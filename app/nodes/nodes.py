from app.prompts import SYSTEM_PROMPT, PLANNER_PROMPT
from app.types.models import Plan
from app.types.state import GameplayState, SrdParserState
from app.tools import make_player_tools
from app.utilities.functions import get_chat_model, get_vector_store
from langchain.agents import create_agent
from langchain.messages import ToolMessage, AIMessage
import os
import re
from typing import cast, Any

def send_message(state: GameplayState) -> dict:
	agent = create_agent(
		model=get_chat_model(),
		tools=make_player_tools(state),
		system_prompt=SYSTEM_PROMPT
	)
	response = agent.invoke(cast(Any, {'messages': state['messages']}))
	return {'messages': response['messages']}

def planner(state: GameplayState) -> dict:
	agent = create_agent(
		model=get_chat_model(),
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
	tool_call_id = str(uuid.uuid4())
	fake_tool_call = AIMessage(content='', tool_calls=[{'name': 'executor', 'args': {}, 'id': tool_call_id}])
	return {'plan': state['plan'], 'messages': state['messages'] + [fake_tool_call, ToolMessage(content=str(state['plan']), name='executor', tool_call_id=tool_call_id)]}

def srd_splitter(state: SrdParserState):
	print(f"Splitting SRD source file: {state['source_file']}")
	splitter_regex = re.compile(r'^#(?!#)\s*(.*?)\s*\n([\s\S]*?)(?=\n#(?!#)\s*|\Z)', re.MULTILINE)
	with open(state['source_file'], 'r', encoding='utf-8') as source:
		sections = splitter_regex.findall(source.read())
	for section, content in sections:
		with open(f'data/temp/{section}.md', 'w', encoding='utf-8') as target:
			target.write(content)
	print(f"SRD source file split into {len(sections)} sections successfully.")
	return {'sections': [section for section, _ in sections]}

def srd_embedder(state: SrdParserState):
	from langchain_text_splitters import MarkdownHeaderTextSplitter
	print('Embedding SRD text...')
	with open('SRD_CC_v5.2.1.md', 'r', encoding='utf-8') as file:
		content = file.read()
	splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[('#', 'Chapter'), ('##', 'Section'), ('###', 'Paragraph')])
	documents = splitter.split_text(content)
	vector_store = get_vector_store()
	vector_store.add_documents(documents)
	print('SRD text embedded successfully.')

def delete_srd_splitted_files(state: SrdParserState):
	for section in state['sections']:
		os.remove(f'data/temp/{section}.md')
	return {}