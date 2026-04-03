from enum import Enum

class AbilityType(Enum):
	STRENGTH = 'Strength'
	DEXTERITY = 'Dexterity'
	CONSTITUTION = 'Constitution'
	INTELLIGENCE = 'Intelligence'
	WISDOM = 'Wisdom'
	CHARISMA = 'Charisma'
	SPEED = 'Speed'

_SIZE_METADATA = {
	'Tiny': 2.5,
	'Small': 5,
	'Medium': 5,
	'Large': 10,
	'Huge': 15,
	'Gargantuan': 20,
}

class Size(Enum):
	TINY = 'Tiny'
	SMALL = 'Small'
	MEDIUM = 'Medium'
	LARGE = 'Large'
	HUGE = 'Huge'
	GARGANTUAN = 'Gargantuan'

	def __init__(self, _: str):
		self.space_feets = _SIZE_METADATA[self.value]

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

_SKILL_METADATA = {
	'Acrobatics': AbilityType.DEXTERITY,
	'Animal Handling': AbilityType.WISDOM,
	'Arcana': AbilityType.INTELLIGENCE,
	'Athletics': AbilityType.STRENGTH,
	'Deception': AbilityType.CHARISMA,
	'History': AbilityType.INTELLIGENCE,
	'Insight': AbilityType.WISDOM,
	'Intimidation': AbilityType.CHARISMA,
	'Investigation': AbilityType.INTELLIGENCE,
	'Medicine': AbilityType.WISDOM,
	'Nature': AbilityType.INTELLIGENCE,
	'Perception': AbilityType.WISDOM,
	'Performance': AbilityType.CHARISMA,
	'Persuasion': AbilityType.CHARISMA,
	'Religion': AbilityType.INTELLIGENCE,
	'Sleight of Hand': AbilityType.DEXTERITY,
	'Stealth': AbilityType.DEXTERITY,
	'Survival': AbilityType.WISDOM
}

class Skill(Enum):
	ACROBATICS = 'Acrobatics'
	ANIMAL_HANDLING = 'Animal Handling'
	ARCANA = 'Arcana'
	ATHLETICS = 'Athletics'
	DECEPTION = 'Deception'
	HISTORY = 'History'
	INSIGHT = 'Insight'
	INTIMIDATION = 'Intimidation'
	INVESTIGATION = 'Investigation'
	MEDICINE = 'Medicine'
	NATURE = 'Nature'
	PERCEPTION = 'Perception'
	PERFORMANCE = 'Performance'
	PERSUASION = 'Persuasion'
	RELIGION = 'Religion'
	SLEIGHT_OF_HAND = 'Sleight of Hand'
	STEALTH = 'Stealth'
	SURVIVAL = 'Survival'

	def __init__(self, _: str):
		self.ability_type = _SKILL_METADATA[self.value]

_LANGUAGE_METADATA = {
	'Common': False,
	'Common (Sign Language)': False,
	'Draconic': False,
	'Dwarvish': False,
	'Elvish': False,
	'Giant': False,
	'Gnomish': False,
	'Goblin': False,
	'Halfling': False,
	'Orc': False,
	'Abyssal': True,
	'Celestial': True,
	'Deep Speech': True,
	'Druidic': True,
	'Infernal': True,
	'Primordial': True,
	'Sylvan': True,
	'Thieves\' Cant': True,
	'Undercommon': True,
}

class Language(Enum):
	COMMON = 'Common'
	COMMON_SIGN_LANGUAGE = 'Common (Sign Language)'
	DRACONIC = 'Draconic'
	DWARVISH = 'Dwarvish'
	ELVISH = 'Elvish'
	GIANT = 'Giant'
	GNOMISH = 'Gnomish'
	GOBLIN = 'Goblin'
	HALFLING = 'Halfling'
	ORC = 'Orc'
	ABYSSAL = 'Abyssal'
	CELESTIAL = 'Celestial'
	DEEP_SPEECH = 'Deep Speech'
	DRUIDIC = 'Druidic'
	INFERNAL = 'Infernal'
	PRIMORDIAL = 'Primordial'
	SYLVAN = 'Sylvan'
	THIEVES_CANT = 'Thieves\' Cant'
	UNDERCOMMON = 'Undercommon'

	def __init__(self, _: str):
		self.is_exotic = _LANGUAGE_METADATA[self.value]

class Alignment(Enum):
	Unaligned = 'Unaligned'
	LawfulGood = 'Lawful Good'
	NeutralGood = 'Neutral Good'
	ChaoticGood = 'Chaotic Good'
	LawfulNeutral = 'Lawful Neutral'
	Neutral = 'Neutral'
	ChaoticNeutral = 'Chaotic Neutral'
	LawfulEvil = 'Lawful Evil'
	NeutralEvil = 'Neutral Evil'
	ChaoticEvil = 'Chaotic Evil'

class Speed(Enum):
	Walk = 'Walk'
	Climbing = 'Climbing'
	Crawling = 'Crawling'
	Flying = 'Flying'
	Jumping = 'Jumping'
	Swimming = 'Swimming'
	Burrowing = 'Burrowing'

_DAMAGE_TYPE_METADATA = {
	'Acid': 'Corrosive liquids, digestive enzymes',
	'Bludgeoning': 'Blunt objects, constriction, falling',
	'Cold': 'Freezing water, icy blasts',
	'Fire': 'Flames, unbearable heat',
	'Force': 'Pure magical energy',
	'Lightning': 'Electricity',
	'Necrotic': 'Life-draining energy',
	'Piercing': 'Fangs, puncturing objects',
	'Poison': 'Toxic gas, venom',
	'Psychic': 'Mind-rendering energy',
	'Radiant': 'Holy energy, searing radiation',
	'Slashing': 'Claws, cutting objects',
	'Thunder': 'Concussive sound'
}

class DamageType(Enum):
	ACID = 'Acid'
	BLUDGEONING = 'Bludgeoning'
	COLD = 'Cold'
	FIRE = 'Fire'
	FORCE = 'Force'
	LIGHTNING = 'Lightning'
	NECROTIC = 'Necrotic'
	PIERCING = 'Piercing'
	POISON = 'Poison'
	PSYCHIC = 'Psychic'
	RADIANT = 'Radiant'
	SLASHING = 'Slashing'
	THUNDER = 'Thunder'

	def __init__(self, _: str):
		self.examples = _DAMAGE_TYPE_METADATA[self.value]