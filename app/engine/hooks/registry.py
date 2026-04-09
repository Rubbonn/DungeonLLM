from enum import Enum
from typing import Callable

class HOOK_LIST(str, Enum):
	ABILITY_CHECK_PRE_ROLL = 'ability_check-pre_roll'
	ABILITY_CHECK_PRE_CALCULATION = 'ability_check-pre_calculation'
	ABILITY_CHECK_POST_CALCULATION = 'ability_check-post_calculation'
	ABILITY_MODIFIER_CALCULATION = 'ability_modifier-calculation'

class HookRegistry:
	def __init__(self):
		self._hooks: dict[HOOK_LIST, list[Callable]] = {hook: [] for hook in HOOK_LIST}

	def register_hook(self, hook_name: HOOK_LIST) -> Callable:
		def decorator(func: Callable) -> Callable:
			self.register_hook_function(hook_name, func)
			return func
		return decorator

	def execute_hooks(self, hook_name: HOOK_LIST, *args, **kwargs) -> None:
		if hook_name not in self._hooks:
			raise ValueError(f'Hook {hook_name} is not a valid hook')
		
		for func in self._hooks[hook_name]:
			func(*args, **kwargs)

	def register_hook_function(self, hook_name: HOOK_LIST, func: Callable) -> None:
		if hook_name not in self._hooks:
			raise ValueError(f'Hook {hook_name} is not a valid hook')

		self._hooks[hook_name].append(func)

global_hook_registry = HookRegistry()