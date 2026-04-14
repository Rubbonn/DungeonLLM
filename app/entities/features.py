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

class WeaponCategory(Enum):
	SIMPLE_MELEE = 'Simple Melee'
	SIMPLE_RANGED = 'Simple Ranged'
	MARTIAL_MELEE = 'Martial Melee'
	MARTIAL_RANGED = 'Martial Ranged'

_WEAPON_PROPERTY_METADATA = {
	'Ammunition': 'You can use a weapon that has the Ammunition property to make a ranged attack only if you have ammunition to fire from it. The type of ammunition required is specified with the weapon\'s range. Each attack expends one piece of ammunition. Drawing the ammunition is part of the attack (you need a free hand to load a one-handed weapon). After a fight, you can spend 1 minute to recover half the ammunition (round down) you used in the fight; the rest is lost.',
	'Finesse': 'When making an attack with a Finesse weapon, use your choice of your Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls.',
	'Heavy': 'You have Disadvantage on attack rolls with a Heavy weapon if it\'s a Melee weapon and your Strength score isn\'t at least 13 or if it\'s a Ranged weapon and your Dexterity score isn\'t at least 13.',
	'Light': 'When you take the Attack action on your turn and attack with a Light weapon, you can make one extra attack as a Bonus Action later on the same turn. That extra attack must be made with a different Light weapon, and you don\'t add your ability modifier to the extra attack\'s damage unless that modifier is negative. For example, you can attack with a Shortsword in one hand and a Dagger in the other using the Attack action and a Bonus Action, but you don\'t add your Strength or Dexterity modifier to the damage roll of the Bonus Action unless that modifier is negative.',
	'Loading': 'You can fire only one piece of ammunition from a Loading weapon when you use an action, a Bonus Action, or a Reaction to fire it, regardless of the number of attacks you can normally make.',
	'Range': 'A Range weapon has a range in parentheses after the Ammunition or Thrown property. The range lists two numbers. The first is the weapon\'s normal range in feet, and the second is the weapon\'s long range. When attacking a target beyond normal range, you have Disadvantage on the attack roll. You can\'t attack a target beyond the long range.',
	'Reach': 'A Reach weapon adds 5 feet to your reach when you attack with it, as well as when determining your reach for Opportunity Attacks with it.',
	'Thrown': 'If a weapon has the Thrown property, you can throw the weapon to make a ranged attack, and you can draw that weapon as part of the attack. If the weapon is a Melee weapon, use the same ability modifier for the attack and damage rolls that you use for a melee attack with that weapon.',
	'Two-Handed': 'A Two-Handed weapon requires two hands when you attack with it.',
	'Versatile': 'A Versatile weapon can be used with one or two hands. A damage value in parentheses appears with the property. The weapon deals that damage when used with two hands to make a melee attack.'
}

class WeaponProperty(Enum):
	AMMUNITION = 'Ammunition'
	FINESSE = 'Finesse'
	HEAVY = 'Heavy'
	LIGHT = 'Light'
	LOADING = 'Loading'
	RANGE = 'Range'
	REACH = 'Reach'
	THROWN = 'Thrown'
	TWO_HANDED = 'Two-Handed'
	VERSATILE = 'Versatile'

	def __init__(self, _: str):
		self.description = _WEAPON_PROPERTY_METADATA[self.value]
		self.is_ranged = self.value == 'Range' or self.value == 'Thrown'

_WEAPON_MASTERY_PROPERTY_METADATA = {
	'Cleave': 'If you hit a creature with a melee attack roll using this weapon, you can make a melee attack roll with the weapon against a second creature within 5 feet of the first that is also within your reach. On a hit, the second creature takes the weapon\'s damage, but don\'t add your ability modifier to that damage unless that modifier is negative. You can make this extra attack only once per turn.',
	'Graze': 'If your attack roll with this weapon misses a creature, you can deal damage to that creature equal to the ability modifier you used to make the attack roll. This damage is the same type dealt by the weapon, and the damage can be increased only by increasing the ability modifier.',
	'Nick': 'When you make the extra attack of the Light property, you can make it as part of the Attack action instead of as a Bonus Action. You can make this extra attack only once per turn.',
	'Push': 'If you hit a creature with this weapon, you can push the creature up to 10 feet straight away from yourself if it is Large or smaller.',
	'Sap': 'If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.',
	'Slow': 'If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn\'t exceed 10 feet.',
	'Topple': 'If you hit a creature with this weapon, you can force the creature to make a Constitution saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.',
	'Vex': 'If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.'
}

class WeaponMasteryProperty(Enum):
	CLEAVE = 'Cleave'
	GRAZE = 'Graze'
	NICK = 'Nick'
	PUSH = 'Push'
	SAP = 'Sap'
	SLOW = 'Slow'
	TOPPLE = 'Topple'
	VEX = 'Vex'

	def __init__(self, _: str):
		self.description = _WEAPON_MASTERY_PROPERTY_METADATA[self.value]