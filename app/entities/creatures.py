import app.entities.features as features
from app.utilities.jsonable import Jsonable
from dataclasses import dataclass
from langchain.tools import tool
from typing import Literal

@dataclass
class Creature(Jsonable):
	name: str
	size: features.Size
	abilities: dict[Literal['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma', 'Speed', 'Initiative'], features.Ability]

	def get_bio(self) -> str:
		return f'Name: {self.name}\nSize: {self.size.value}'
	
	def get_abilities(self) -> str:
		return '\n'.join([f'{value.name.value}: {value.value}' for ability, value in self.abilities.items()])

@dataclass
class Player(Creature):
	pass