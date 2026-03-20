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

def gear_parser(state: SrdParserState):
	if not 'Equipment' in state['sections']:
		return {}
	
	extraction_regex = re.compile(r'^##(?!#)\s*Adventuring Gear\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}
	
	llm = init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER')).with_structured_output({
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
	}, method='json_schema')
	response = llm.invoke(f'''Extract the gear items from the following text, providing their name, weight, cost and description in the following JSON Schema format:
	{{
		'type': 'array',
		'title': 'Gear Items',
		'description': 'List of gear items with their properties',
		'items': {{
			'type': 'object',
			'properties': {{
				'name': {{'type': 'string', 'description': 'The name of the gear item'}},
				'weight': {{'type': 'number', 'description': 'The weight of the gear item in pounds'}},
				'cost': {{'type': 'number', 'description': 'The cost of the gear item in gold pieces'}},
				'description': {{'type': 'string', 'description': 'A brief description of the gear item'}}
			}}
		}}
	}}

	Text to extract from:
	{match.group(1)}
	''')
	print(response)