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

class Skill(Enum):
	ACROBATICS = ('Acrobatics', AbilityType.DEXTERITY)
	ANIMAL_HANDLING = ('Animal Handling', AbilityType.WISDOM)
	ARCANA = ('Arcana', AbilityType.INTELLIGENCE)
	ATHLETICS = ('Athletics', AbilityType.STRENGTH)
	DECEPTION = ('Deception', AbilityType.CHARISMA)
	HISTORY = ('History', AbilityType.INTELLIGENCE)
	INSIGHT = ('Insight', AbilityType.WISDOM)
	INTIMIDATION = ('Intimidation', AbilityType.CHARISMA)
	INVESTIGATION = ('Investigation', AbilityType.INTELLIGENCE)
	MEDICINE = ('Medicine', AbilityType.WISDOM)
	NATURE = ('Nature', AbilityType.INTELLIGENCE)
	PERCEPTION = ('Perception', AbilityType.WISDOM)
	PERFORMANCE = ('Performance', AbilityType.CHARISMA)
	PERSUASION = ('Persuasion', AbilityType.CHARISMA)
	RELIGION = ('Religion', AbilityType.INTELLIGENCE)
	SLEIGHT_OF_HAND = ('Sleight of Hand', AbilityType.DEXTERITY)
	STEALTH = ('Stealth', AbilityType.DEXTERITY)
	SURVIVAL = ('Survival', AbilityType.WISDOM)