from app.types.planning import Plan
from app.types.state import State
from app.tools import tools_list
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

def send_message(state: State) -> dict:
	chat_model = init_chat_model(model='qwen3.5:397b-cloud', model_provider='ollama').bind_tools(tools_list)
	response = chat_model.invoke(state['messages'])
	return {'messages': [response]}

def planner(state: State) -> dict:
	def get_player_info() -> str:
		'''
		Returns a string containing the player's name, size, and abilities.

		Returns:
			str: A string containing the player's name, size, and abilities.
		'''
		return f'{state['player'].get_bio()}\n{state['player'].get_abilities()}'
	
	agent = create_agent(
		model=init_chat_model(model='qwen3.5:397b-cloud', model_provider='ollama'),
		tools=tools_list + [get_player_info],
		response_format=Plan
	)
	response = agent.invoke({'messages': state['messages'] + [{'type': 'user', 'content': 'Before proceeding with the narration, analyze the current situation and generate an ordered list of the actions that are immediately necessary. Include only truly necessary actions; avoid optional or speculative actions. If no actions are necessary at this moment, explicitly return an empty list.'}]})
	return {'plan': response['structured_response']}
