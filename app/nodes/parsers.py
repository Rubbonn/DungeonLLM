from app.database import get_database_session
from app.types.models import GearItems, DamageTypes, WeaponProperties, WeaponMasteryProperties, Weapons
from app.types.state import SrdParserState
from app.utilities.functions import retry_exception
from langchain.chat_models import init_chat_model
from os import environ
import re

def gear_parser(state: SrdParserState) -> dict:
	from app.entities.items import Gear
	if not 'Equipment' in state['sections'] or not Gear.is_empty():
		return {}

	print(f"Parsing gear items...")
	extraction_regex = re.compile(r'^##(?!#)\s*Adventuring Gear\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}

	llm = init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER'),
	                      max_completion_tokens=32768).with_structured_output(GearItems)
	response: GearItems = retry_exception(func=llm.invoke, input=f'''Extract the gear items from the following text, providing their name, weight, cost and description:
	{match.group(1)}
	''')
	if len(response.items) == 0:
		raise Exception('No gear items found in the text')

	session = get_database_session()
	for item in response.items:
		gear_item = Gear(name=item.name, weight=item.weight, cost=item.cost, description=item.description)
		session.add(gear_item)
	session.commit()
	print("Gear items parsing completed successfully.")
	return {}


def weapons_parser(state: SrdParserState) -> dict:
	if not 'Equipment' in state['sections'] or not 'Rules Glossary' in state['sections']:
		return {}

	print(f"Parsing weapons and related entities...")
	llm = init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER'),
	                      max_completion_tokens=32768)
	session = get_database_session()

	# Damage types extraction
	from app.entities.items import DamageType
	if DamageType.is_empty():
		print("Extracting damage types...")
		extraction_regex = re.compile(r'^###(?!#)\s*Damage Types\s*\n([\s\S]*?)(?=\n###(?!#)\s*|\Z)', re.MULTILINE)
		with open('data/temp/Rules Glossary.md', 'r', encoding='utf-8') as source:
			match = extraction_regex.search(source.read())
		if match:
			llm_with_structured_output = llm.with_structured_output(DamageTypes)
			response: DamageTypes = retry_exception(func=llm_with_structured_output.invoke, input=f'''Extract the damage types from the following text, providing their name and examples:
			{match.group(1)}
			''')
			if len(response.items) == 0:
				raise Exception('No damage types found in the text')

			for item in response.items:
				damage_type = DamageType(name=item.name, examples=item.examples)
				session.add(damage_type)
			session.commit()

	extraction_regex = re.compile(r'^##(?!#)\s*Weapons\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}

	# Weapon properties extraction
	from app.entities.items import WeaponProperty
	if WeaponProperty.is_empty():
		print("Extracting weapon properties...")
		llm_with_structured_output = llm.with_structured_output(WeaponProperties)
		response: WeaponProperties = retry_exception(func=llm_with_structured_output.invoke, input=f'''Extract the weapon properties (excluding the mastery properties) from the following text, providing their name and description:
		{match.group(1)}
		''')
		if len(response.items) == 0:
			raise Exception('No weapon properties found in the text')

		for item in response.items:
			weapon_property = WeaponProperty(name=item.name, description=item.description)
			session.add(weapon_property)
		session.commit()

	# Weapon mastery properties extraction
	from app.entities.items import WeaponMasteryProperty
	if WeaponMasteryProperty.is_empty():
		print("Extracting weapon mastery properties...")
		llm_with_structured_output = llm.with_structured_output(WeaponMasteryProperties)
		response: WeaponMasteryProperties = retry_exception(func=llm_with_structured_output.invoke, input=f'''Extract the weapon mastery properties (excluding the normal properties) from the following text, providing their name and description:
		{match.group(1)}
		''')
		if len(response.items) == 0:
			raise Exception('No weapon mastery properties found in the text')

		for item in response.items:
			weapon_mastery_property = WeaponMasteryProperty(name=item.name, description=item.description)
			session.add(weapon_mastery_property)
		session.commit()

	# Weapons extraction
	from app.entities.items import Weapon
	if Weapon.is_empty():
		print("Extracting weapons...")
		llm_with_structured_output = llm.with_structured_output(Weapons)
		response: Weapons = retry_exception(func=llm_with_structured_output.invoke, input=f'''Extract the weapons from the following text, providing their name, description, damage, damage type, properties, mastery property, weight, and cost:
			{match.group(1)}
			''')
		if len(response.items) == 0:
			raise Exception('No weapons found in the text')

		from sqlalchemy import select
		for item in response.items:
			damage_type = session.scalar(select(DamageType).filter_by(name=item.damage_type))
			weapon_mastery_property = session.scalar(
				select(WeaponMasteryProperty).filter_by(name=item.mastery_property))
			weapon_properties = session.scalars(
				select(WeaponProperty).where(WeaponProperty.name.in_(item.properties))).all()
			weapon = Weapon(name=item.name, damage=item.damage, damage_type=damage_type,
			                properties=weapon_properties, mastery_property=weapon_mastery_property,
			                weight=item.weight, cost=item.cost)
			session.add(weapon)
		session.commit()

	print("Weapons parsing completed successfully.")
	return {}