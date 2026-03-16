from typing import Literal

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