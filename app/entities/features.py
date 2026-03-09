from abc import ABC
from app.utilities.jsonable import Jsonable
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class Ability(ABC, Jsonable):
	name: str
	value: int

@dataclass
class Strength(Ability):
	name: str = field(default='Strength', init=False)

@dataclass
class Dexterity(Ability):
	name: str = field(default='Dexterity', init=False)

@dataclass
class Constitution(Ability):
	name: str = field(default='Constitution', init=False)

@dataclass
class Intelligence(Ability):
	name: str = field(default='Intelligence', init=False)

@dataclass
class Wisdom(Ability):
	name: str = field(default='Wisdom', init=False)

@dataclass
class Charisma(Ability):
	name: str = field(default='Charisma', init=False)

@dataclass
class Speed(Ability):
	name: str = field(default='Speed', init=False)

@dataclass
class Initiative(Ability):
	name: str = field(default='Initiative', init=False)

class Size(Enum):
	TINY = ("Tiny", 2.5)
	SMALL = ("Small", 5)
	MEDIUM = ("Medium", 5)
	LARGE = ("Large", 10)
	HUGE = ("Huge", 15)
	GARGANTUAN = ("Gargantuan", 20)

	def __init__(self, label: str, space_feets: float):
		self.label = label
		self.space_feets = space_feets

	@property
	def space_feets_squared(self) -> float:
		return self.space_feets ** 2

	@property
	def space_squares(self) -> float:
		return self.space_feets / 5

	@property
	def space_squares_squared(self) -> float:
		return self.space_squares ** 2

	def __repr__(self):
		properties = ', '.join([f'{prop}={self.__getattribute__(prop)}' for prop in self.__dir__() if not prop.startswith('_')])
		return f'{self.__class__.__name__}({properties})'