from app.types.state import State
from langchain.tools import tool
from typing import Literal

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

@tool
def throw_dice(sides: Literal[4, 6, 8, 10, 12, 20, 100]) -> int:
	'''
	Rolls a die with the specified number of sides and returns the result.

	Args:
		sides (Literal[4, 6, 8, 10, 12, 20, 100]): The number of sides on the die. Must be one of the following: 4, 6, 8, 10, 12, 20, or 100.
	
	Returns:
		int: The result of the die roll, which will be a random integer between 1 and the number of sides (inclusive).
	'''
	if sides not in [4, 6, 8, 10, 12, 20, 100]:
		raise ValueError("Invalid number of sides. Must be one of the following: 4, 6, 8, 10, 12, 20, or 100.")
	
	from random import randint
	return randint(1, sides)

tools_list = [throw_dice]