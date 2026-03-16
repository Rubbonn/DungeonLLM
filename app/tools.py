from app.types.state import State
from langchain.tools import tool

def make_player_tools(state: State) -> list:
	@tool
	def get_player_info() -> str:
		'''
		Returns a string containing the player's name, size, and abilities.

		Returns:
			str: A string containing the player's name, size, and abilities.
		'''
		return f'{state['player'].get_bio()}\n{state['player'].get_abilities()}'

	return [get_player_info]

tools_list = []