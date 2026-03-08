from abc import ABC
from dataclasses import dataclass, field

@dataclass
class Ability(ABC):
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

class Size(ABC):
	name: str
	space_feets: float
	space_feets_squared: float
	space_squares: float
	space_squares_squared: float

	def __repr__(self):
		return f'{self.__class__.__name__}(name={self.name}, space_feets={self.space_feets}, space_feets_squared={self.space_feets_squared}, space_squares={self.space_squares}, space_squares_squared={self.space_squares_squared})'

class Tiny(Size):
	name = 'Tiny'
	space_feets = 2.5
	space_feets_squared = 6.25
	space_squares = 0.25
	space_squares_squared = 0.0625

class Small(Size):
	name = 'Small'
	space_feets = 5
	space_feets_squared = 25
	space_squares = 1
	space_squares_squared = 1

class Medium(Size):
	name = 'Medium'
	space_feets = 5
	space_feets_squared = 25
	space_squares = 1
	space_squares_squared = 1

class Large(Size):
	name = 'Large'
	space_feets = 10
	space_feets_squared = 100
	space_squares = 4
	space_squares_squared = 16

class Huge(Size):
	name = 'Huge'
	space_feets = 15
	space_feets_squared = 225
	space_squares = 9
	space_squares_squared = 81

class Gargantuan(Size):
	name = 'Gargantuan'
	space_feets = 20
	space_feets_squared = 400
	space_squares = 16
	space_squares_squared = 256