from enum import Enum
from typing import Callable

class HOOK_LIST(str, Enum):
	pass

class HookRegistry:
	_hooks: dict[HOOK_LIST, list[Callable]] = {hook: [] for hook in HOOK_LIST}

	@classmethod
	def register_hook(cls, hook_name: HOOK_LIST):
		def decorator(func: Callable):
			if hook_name not in cls._hooks:
				raise ValueError(f'Hook {hook_name} is not a valid hook')
			
			cls._hooks[hook_name].append(func)
			return func
		return decorator

	@classmethod
	def execute_hooks(cls, hook_name: HOOK_LIST, *args, **kwargs):
		if hook_name not in cls._hooks:
			raise ValueError(f'Hook {hook_name} is not a valid hook')
		
		for func in cls._hooks[hook_name]:
			func(*args, **kwargs)