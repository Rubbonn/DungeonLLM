from enum import Enum

class AbilityType(Enum):
	STRENGTH = 'Strength'
	DEXTERITY = 'Dexterity'
	CONSTITUTION = 'Constitution'
	INTELLIGENCE = 'Intelligence'
	WISDOM = 'Wisdom'
	CHARISMA = 'Charisma'
	SPEED = 'Speed'
	INITIATIVE = 'Initiative'

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

class CreatureType(Enum):
	ABERRATION = 'Aberration'
	BEAST = 'Beast'
	CELESTIAL = 'Celestial'
	CONSTRUCT = 'Construct'
	DRAGON = 'Dragon'
	ELEMENTAL = 'Elemental'
	FEY = 'Fey'
	FIEND = 'Fiend'
	GIANT = 'Giant'
	HUMANOID = 'Humanoid'
	MONSTROSITY = 'Monstrosity'
	OOZE = 'Ooze'
	PLANT = 'Plant'
	UNDEAD = 'Undead'