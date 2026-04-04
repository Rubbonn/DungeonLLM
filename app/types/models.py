import app.entities.features as features
from app.types.actions import AbilityCheckAction
from pydantic import BaseModel, Field


class GearItem(BaseModel):
	name: str = Field(description='The name of the gear item')
	weight: float = Field(description='The weight of the gear item in pounds')
	cost: float = Field(description='The cost of the gear item in gold pieces')
	description: str = Field(description='A brief description of the gear item')


class GearItems(BaseModel):
	items: list[GearItem] = Field(description='List of gear items with their properties', default_factory=list)


class Weapon(BaseModel):
	name: str = Field(description='The name of the weapon')
	damage: str = Field(description='The damage of the weapon')
	damage_type: features.DamageType = Field(description='The damage type of the weapon')
	versatile_damage: str | None = Field(description='The versatile damage of the weapon if it has versatile damage, otherwise None')
	properties: set[features.WeaponProperty] = Field(description='A list of properties of the weapon', default_factory=set)
	mastery_property: features.WeaponMasteryProperty = Field(description='The mastery property of the weapon')
	range: int | None = Field(description='The range of the weapon in feet if it has a range, otherwise None')
	long_range: int | None = Field(description='The long range of the weapon in feet if it has a long range, otherwise None')
	ammunition: str | None = Field(description='The type of ammunition used by the weapon if it has ammunition, otherwise None')
	weight: float = Field(description='The weight of the item in pounds')
	cost: float = Field(description='The cost of the item in gold pieces')


class Weapons(BaseModel):
	items: list[Weapon] = Field(description='A list of weapons in the SRD', default_factory=list)

class Tool(BaseModel):
	name: str = Field(description='The name of the tool')
	weight: float = Field(description='The weight of the item in pounds')
	cost: float = Field(description='The cost of the item in gold pieces')
	ability: features.AbilityType = Field(description='The ability of the tool for ability checks')
	utilize: str = Field(description='Uses for the tool and their DC')
	craft: list[GearItem] = Field(description='Gear items that can be crafted with the tool', default_factory=list)

class Tools(BaseModel):
	items: list[Tool] = Field(description='A list of tools in the SRD', default_factory=list)

class AnimalSpeed(BaseModel):
	speed: int = Field(description='The speed value in feet')
	conditions: str = Field(description='Any conditions that apply to this speed (e.g. "only when climbing")', default='')

class Armor(BaseModel):
	name: str = Field(description='The name of the armor')
	weight: float = Field(description='The weight of the item in pounds')
	cost: float = Field(description='The cost of the item in gold pieces')
	minutes_to_equip: int = Field(description='The time in minutes required to equip the armor')
	minutes_to_unequip: int = Field(description='The time in minutes required to unequip the armor')
	armor_class: int = Field(description='The armor class provided by the armor')
	dexterity_add: bool = Field(description='Whether the armor allows adding dexterity to armor class')
	max_dexterity_bonus: int | None = Field(description='The maximum dexterity bonus allowed by the armor, if any')
	minimum_strength: int | None = Field(description='The minimum strength required to wear the armor, if any')
	has_stealth_disadvantage: bool = Field(description='Whether the armor imposes disadvantage on stealth checks')

class Armors(BaseModel):
	items: list[Armor] = Field(description='A list of armors in the SRD', default_factory=list)


class Animal(BaseModel):
	name: str = Field(description='The name of the animal')
	size: features.Size = Field(description='The size of the animal')
	creature_type: features.CreatureType = Field(description='The creature type of the animal')
	creature_sub_type: str = Field(description='The creature subtype of the animal')
	alignment: features.Alignment = Field(description='The alignment of the animal')
	armor_class: int = Field(description='The armor class of the animal')
	hit_points: int = Field(description='The average hit points of the animal')
	hit_points_formula: str = Field(description='The hit points formula of the animal (e.g. 1d6+1)')
	speed: dict[features.Speed, AnimalSpeed] = Field(description='The speed of the animal by movement type, with value in feet and any conditions', default_factory=dict)
	abilities: dict[features.AbilityType, tuple[int, int, int]] = Field(description='The ability scores of the animal, with each tuple containing (score, modifier, save_modifier)', default_factory=dict)
	skill_proficiencies: dict[features.Skill, int] = Field(description='The skill proficiencies of the animal and their associated bonuses', default_factory=dict)
	languages: list[features.Language] = Field(description='The languages known by the animal', default_factory=list)
	challenge_rating: float = Field(description='The challenge rating of the animal')
	experience_points: int = Field(description='The experience points awarded for defeating the animal')
	initiative_bonus: int = Field(description='The initiative bonus of the animal')
	traits: dict[str, str] = Field(description='The animal traits names and their description', default_factory=dict)

class Animals(BaseModel):
	items: list[Animal] = Field(description='A list of animals in the SRD', default_factory=list)

class Plan(BaseModel):
	actions: list[AbilityCheckAction] = Field(description='A list of actions to execute.', default_factory=list)

	def __str__(self) -> str:
		if len(self.actions) == 0:
			return 'No actions in the plan.'
		
		plan_str = 'Actions executed:\n|Action|Reason|Result|\n|-|-|-|\n'
		return plan_str + '\n'.join([f'|{action.action}|{action.reason}|{action.result}|' for action in self.actions])