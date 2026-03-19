import app.entities.features as features
from app.utilities.jsonable import Jsonable
from dataclasses import dataclass

@dataclass
class Creature(Jsonable):
	name: str
	size: features.Size
	abilities: dict[features.AbilityType, features.Ability]

	def get_bio(self) -> str:
		return f'Name: {self.name}\nSize: {self.size.value}'
	
	def get_abilities(self) -> str:
		return '\n'.join([f'{ability}: {value.value}' for ability, value in self.abilities.items()])

	def get_ability_modifier(self, ability: features.AbilityType) -> int:
		match self.abilities[ability].value:
			case 1:
				return -5
			case 2 | 3:
				return -4
			case 4 | 5:
				return -3
			case 6 | 7:
				return -2
			case 8 | 9:
				return -1
			case 10 | 11:
				return 0
			case 12 | 13:
				return 1
			case 14 | 15:
				return 2
			case 16 | 17:
				return 3
			case 18 | 19:
				return 4
			case 20 | 21:
				return 5
			case 22 | 23:
				return 6
			case 24 | 25:
				return 7
			case 26 | 27:
				return 8
			case 28 | 29:
				return 9
			case 30:
				return 10
			case _:
				raise ValueError('Invalid ability value')

@dataclass
class Player(Creature):
	pass