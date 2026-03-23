from app.database import get_database_session
from app.prompts import SYSTEM_PROMPT, PLANNER_PROMPT
from app.types.planning import Plan
from app.types.state import GameplayState, SrdParserState
from app.tools import make_player_tools
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import ToolMessage
from os import environ
import re
from typing import cast, Any

def send_message(state: GameplayState) -> dict:
	agent = create_agent(
		model=init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER')),
		tools=make_player_tools(state),
		system_prompt=SYSTEM_PROMPT
	)
	response = agent.invoke(cast(Any, {'messages': state['messages']}))
	return {'messages': response['messages']}

def planner(state: GameplayState) -> dict:
	agent = create_agent(
		model=init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER')),
		system_prompt=PLANNER_PROMPT,
		response_format=Plan
	)
	response = agent.invoke(cast(Any, {'messages': state['messages']}))
	return {'plan': response['structured_response']}

def executor(state: GameplayState) -> dict:
	assert state['plan'] is not None
	if len(state['plan'].actions) == 0:
		return {}

	for action in state['plan'].actions:
		action.execute(state)
	import uuid
	return {'plan': state['plan'], 'messages': ToolMessage(content=str(state['plan']), name='executor', tool_call_id=str(uuid.uuid4()))}

def srd_splitter(state: SrdParserState):
	splitter_regex = re.compile(r'^#(?!#)\s*(.*?)\s*\n([\s\S]*?)(?=\n#(?!#)\s*|\Z)', re.MULTILINE)
	with open(state['source_file'], 'r', encoding='utf-8') as source:
		sections = splitter_regex.findall(source.read())
	for section, content in sections:
		with open(f'data/temp/{section}.md', 'w', encoding='utf-8') as target:
			target.write(content)
	return {'sections': [section for section, _ in sections]}

def gear_parser(state: SrdParserState) -> dict:
	if not 'Equipment' in state['sections']:
		return {}
	
	extraction_regex = re.compile(r'^##(?!#)\s*Adventuring Gear\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}

	llm = init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER'), max_completion_tokens=32768).with_structured_output({
		'type': 'array',
		'title': 'Gear Items',
		'description': 'List of gear items with their properties',
		'items': {
			'type': 'object',
			'properties': {
				'name': {'type': 'string', 'description': 'The name of the gear item'},
				'weight': {'type': 'number', 'description': 'The weight of the gear item in pounds'},
				'cost': {'type': 'number', 'description': 'The cost of the gear item in gold pieces'},
				'description': {'type': 'string', 'description': 'A brief description of the gear item'}
			}
		}
	})
	response = llm.invoke(f'''Extract the gear items from the following text, providing their name, weight, cost and description:
	{match.group(1)}
	''')
	if len(response) == 0:
		raise Exception('No gear items found in the text')

	from app.entities.items import Gear
	session = get_database_session()
	for item in response:
		gear_item = Gear(name=item['name'], weight=item['weight'], cost=item['cost'], description=item['description'])
		session.add(gear_item)
	session.commit()
	return {}

def weapons_parser(state: SrdParserState) -> dict:
	if not 'Equipment' in state['sections'] or not 'Rules Glossary' in state['sections']:
		return {}

	llm = init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER'), max_completion_tokens=32768)
	session = get_database_session()

	# Damage types extraction
	extraction_regex = re.compile(r'^###(?!#)\s*Damage Types\s*\n([\s\S]*?)(?=\n###(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Rules Glossary.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if match:
		llm_with_structured_output = llm.with_structured_output({
			'type': 'array',
			'title': 'Damage Types',
			'description': 'A list of damage types in the SRD',
			'items': {
				'type': 'object',
				'properties': {
					'name': {'type': 'string', 'description': 'The name of the damage type'},
					'examples': {'type': 'string', 'description': 'Examples when the damage type is used in the SRD'}
				}
			}
		})
		response = llm_with_structured_output.invoke(f'''Extract the damage types from the following text, providing their name and examples:
		{match.group(1)}
		''')
		if len(response) == 0:
			raise Exception('No damage types found in the text')

		from app.entities.items import DamageType
		for item in response:
			damage_type = DamageType(name=item['name'], examples=item['examples'])
			session.add(damage_type)

	extraction_regex = re.compile(r'^##(?!#)\s*Weapons\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}

	# Weapon properties extraction
	llm_with_structured_output = llm.with_structured_output({
		'type': 'array',
		'title': 'Weapon Properties',
		'description': 'A list of weapon properties in the SRD',
		'items': {
			'type': 'object',
			'properties': {
				'name': {'type': 'string', 'description': 'The name of the weapon property'},
				'description': {'type': 'string', 'description': 'Description of the weapon property'}
			}
		}
	})
	response = llm_with_structured_output.invoke(f'''Extract the weapon properties (excluding the mastery properties) from the following text, providing their name and description:
	{match.group(1)}
	''')
	if len(response) == 0:
		raise Exception('No weapon properties found in the text')

	from app.entities.items import WeaponProperty
	for item in response:
		weapon_property = WeaponProperty(name=item['name'], description=item['description'])
		session.add(weapon_property)

	# Weapon mastery properties extraction
	llm_with_structured_output = llm.with_structured_output({
		'type': 'array',
		'title': 'Weapon Mastery Properties',
		'description': 'A list of weapon mastery properties in the SRD',
		'items': {
			'type': 'object',
			'properties': {
				'name': {'type': 'string', 'description': 'The name of the weapon mastery property'},
				'description': {'type': 'string', 'description': 'Description of the weapon mastery property'}
			}
		}
	})
	response = llm_with_structured_output.invoke(f'''Extract the weapon mastery properties (excluding the normal properties) from the following text, providing their name and description:
	{match.group(1)}
	''')
	if len(response) == 0:
		raise Exception('No weapon mastery properties found in the text')

	from app.entities.items import WeaponMasteryProperty
	for item in response:
		weapon_mastery_property = WeaponMasteryProperty(name=item['name'], description=item['description'])
		session.add(weapon_mastery_property)

	# Weapons extraction
	llm_with_structured_output = llm.with_structured_output({
		'type': 'array',
		'title': 'Weapons',
		'description': 'A list of weapons in the SRD',
		'items': {
			'type': 'object',
			'properties': {
				'name': {'type': 'string', 'description': 'The name of the weapon'},
				'damage': {'type': 'string', 'description': 'The damage of the weapon'},
				'damage_type': {'type': 'string', 'description': 'The damage type of the weapon'},
				'properties': {
					'type': 'array',
					'description': 'A list of properties of the weapon',
					'items': {'type': 'string', 'description': 'A property of the weapon'}
				},
				'mastery_property': {'type': 'string', 'description': 'The mastery property of the weapon'},
				'weight': {'type': 'number', 'description': 'The weight of the item in pounds'},
				'cost': {'type': 'number', 'description': 'The cost of the item in gold pieces'},
			}
		}
	})
	response = llm_with_structured_output.invoke(f'''Extract the weapons from the following text, providing their name, description, damage, damage type, properties, mastery property, weight, and cost:
		{match.group(1)}
		''')
	if len(response) == 0:
		raise Exception('No weapons found in the text')

	from app.entities.items import Weapon
	from sqlalchemy import select
	for item in response:
		damage_type = session.scalar(select(DamageType).filter_by(name = item['damage_type']))
		weapon_mastery_property = session.scalar(select(WeaponMasteryProperty).filter_by(name = item['mastery_property']))
		weapon_properties = session.scalars(select(WeaponProperty).where(WeaponProperty.name.in_(item['properties'])))
		weapon = Weapon(name=item['name'], description=item['description'], damage=item['damage'], damage_type_id=damage_type.id, properties=item['properties'], mastery_property_id=weapon_mastery_property.id, weight=item['weight'], cost=item['cost'])
		session.add(weapon)

	session.commit()
	return {}