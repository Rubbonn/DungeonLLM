from app.prompts import SYSTEM_PROMPT, PLANNER_PROMPT
from app.types.planning import Plan
from app.types.state import State
from app.tools import make_player_tools
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from typing import cast, Any

def send_message(state: State) -> dict:
	agent = create_agent(
		model=init_chat_model(model='qwen3.5:397b-cloud', model_provider='ollama'),
		tools=make_player_tools(state),
		system_prompt=SYSTEM_PROMPT
	)
	response = agent.invoke(cast(Any, {'messages': state['messages']}))
	return {'messages': response['messages']}

def planner(state: State) -> dict:	
	agent = create_agent(
		model=init_chat_model(model='qwen3.5:397b-cloud', model_provider='ollama'),
		system_prompt=PLANNER_PROMPT,
		response_format=Plan
	)
	response = agent.invoke(cast(Any, {'messages': state['messages']}))
	return {'plan': response['structured_response']}

def executor(state: State) -> dict:
	if len(state['plan'].actions) == 0:
		return {}
	# TODO Eseguire le azioni e memorizzare i risultati
	return {'plan': state['plan']}
