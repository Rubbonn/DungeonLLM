from app.entities.creatures import Creature
from app.entities.features import AbilityType, Skill
from typing import TypedDict, Union, Literal, Optional

class AbilityCheckState(TypedDict):
	num_dices: int
	num_sides: int
	creature: Creature
	operation: Union[Literal['nothing'], Literal['add']]
	ability: AbilityType
	skill: Optional[Skill]
	dc: int
	ability_mod: int
	result: int

class AbilityModifierState(TypedDict):
	ability: AbilityType
	score: int
	modifier: int

class SkillProficiencyState(TypedDict):
	skill: Skill
	level: float
	bonus: int