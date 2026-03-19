from app.prompts import SYSTEM_PROMPT, PLANNER_PROMPT
from app.types.planning import Plan
from app.types.state import State
from app.tools import make_player_tools
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import ToolMessage
from os import environ
from typing import cast, Any
import uuid

def send_message(state: State) -> dict:
	agent = create_agent(
		model=init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER')),
		tools=make_player_tools(state),
		system_prompt=SYSTEM_PROMPT
	)
	response = agent.invoke(cast(Any, {'messages': state['messages']}))
	return {'messages': response['messages']}

def planner(state: State) -> dict:	
	agent = create_agent(
		model=init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER')),
		system_prompt=PLANNER_PROMPT,
		response_format=Plan
	)
	response = agent.invoke(cast(Any, {'messages': state['messages']}))
	return {'plan': response['structured_response']}

def executor(state: State) -> dict:
	assert state['plan'] is not None
	if len(state['plan'].actions) == 0:
		return {}

	for action in state['plan'].actions:
		action.execute(state)
	return {'plan': state['plan'], 'messages': ToolMessage(content=str(state['plan']), name='executor', tool_call_id=str(uuid.uuid4()))}
