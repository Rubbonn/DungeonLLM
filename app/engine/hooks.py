from app.entities.creatures import Creature
from app.entities.features import AbilityType, Skill
from enum import Enum
from typing import Callable, TypedDict, Union, Literal, Optional

class HOOK_LIST(str, Enum):
	ABILITY_CHECK_PRE_ROLL = 'ability_check-pre_roll'
	ABILITY_CHECK_POST_ROLL = 'ability_check-post_roll'
	ABILITY_CHECK_POST_CALCULATION = 'ability_check-post_calculation'
	ABILITY_MODIFIER_CALCULATION = 'ability_modifier-calculation'

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

class HookRegistry:
	_hooks: dict[HOOK_LIST, list[Callable]] = {hook: [] for hook in HOOK_LIST}

	@classmethod
	def register_hook(cls, hook_name: HOOK_LIST) -> Callable:
		def decorator(func: Callable) -> Callable:
			if hook_name not in cls._hooks:
				raise ValueError(f'Hook {hook_name} is not a valid hook')
			
			cls._hooks[hook_name].append(func)
			return func
		return decorator

	@classmethod
	def execute_hooks(cls, hook_name: HOOK_LIST, *args, **kwargs) -> None:
		if hook_name not in cls._hooks:
			raise ValueError(f'Hook {hook_name} is not a valid hook')
		
		for func in cls._hooks[hook_name]:
			func(*args, **kwargs)

	@classmethod
	def register_hook_function(cls, hook_name: HOOK_LIST, func: Callable) -> None:
		if hook_name not in cls._hooks:
			raise ValueError(f'Hook {hook_name} is not a valid hook')

		cls._hooks[hook_name].append(func)