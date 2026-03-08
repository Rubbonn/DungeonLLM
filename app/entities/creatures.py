import app.entities.features as features
from dataclasses import dataclass
from typing import Literal

@dataclass
class Creature:
	name: str
	size: features.Size
	abilities: dict[Literal['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma', 'Speed', 'Initiative'], features.Ability]

@dataclass
class Player(Creature):
	pass