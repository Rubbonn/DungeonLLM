import app.entities.features as features
from app.utilities.jsonable import Jsonable
from dataclasses import dataclass
from typing import Literal

@dataclass
class Creature(Jsonable):
	name: str
	size: features.Size
	abilities: dict[Literal['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma', 'Speed', 'Initiative'], features.Ability]

@dataclass
class Player(Creature):
	pass