from app.entities.features import AbilityType
from app.types.actions import AbilityCheckAction
from pydantic import BaseModel, Field


class GearItem(BaseModel):
	name: str = Field(description='The name of the gear item')
	weight: float = Field(description='The weight of the gear item in pounds')
	cost: float = Field(description='The cost of the gear item in gold pieces')
	description: str = Field(description='A brief description of the gear item')


class GearItems(BaseModel):
	items: list[GearItem] = Field(description='List of gear items with their properties', default_factory=list)


class DamageType(BaseModel):
	name: str = Field(description='The name of the damage type')
	examples: str = Field(description='Examples when the damage type is used in the SRD')


class DamageTypes(BaseModel):
	items: list[DamageType] = Field(description='A list of damage types in the SRD', default_factory=list)


class WeaponProperty(BaseModel):
	name: str = Field(description='The name of the weapon property')
	description: str = Field(description='Description of the weapon property')


class WeaponProperties(BaseModel):
	items: list[WeaponProperty] = Field(description='A list of weapon properties in the SRD', default_factory=list)


class WeaponMasteryProperty(BaseModel):
	name: str = Field(description='The name of the weapon mastery property')
	description: str = Field(description='Description of the weapon mastery property')


class WeaponMasteryProperties(BaseModel):
	items: list[WeaponMasteryProperty] = Field(description='A list of weapon mastery properties in the SRD', default_factory=list)


class Weapon(BaseModel):
	name: str = Field(description='The name of the weapon')
	damage: str = Field(description='The damage of the weapon')
	damage_type: str = Field(description='The damage type of the weapon')
	properties: list[str] = Field(description='A list of properties of the weapon', default_factory=list)
	mastery_property: str = Field(description='The mastery property of the weapon')
	weight: float = Field(description='The weight of the item in pounds')
	cost: float = Field(description='The cost of the item in gold pieces')


class Weapons(BaseModel):
	items: list[Weapon] = Field(description='A list of weapons in the SRD', default_factory=list)

class Tool(BaseModel):
	name: str = Field(description='The name of the tool')
	weight: float = Field(description='The weight of the item in pounds')
	cost: float = Field(description='The cost of the item in gold pieces')
	ability: AbilityType = Field(description='The ability of the tool for ability checks')
	utilize: str = Field(description='Uses for the tool and their DC')
	craft: list[GearItem] = Field(description='Gear items that can be crafted with the tool', default_factory=list)

class Tools(BaseModel):
	items: list[Tool] = Field(description='A list of tools in the SRD', default_factory=list)

class Plan(BaseModel):
	actions: list[AbilityCheckAction] = Field(description='A list of actions to execute.', default_factory=list)

	def __str__(self) -> str:
		if len(self.actions) == 0:
			return 'No actions in the plan.'
		
		plan_str = 'Actions executed:\n|Action|Reason|Result|\n|-|-|-|\n'
		return plan_str + '\n'.join([f'|{action.action}|{action.reason}|{action.result}|' for action in self.actions])