from langchain_core.language_models.chat_models import BaseChatModel
from langchain.chat_models import init_chat_model
from os import environ
from typing import Literal, Callable, TypeVar, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

def throw_dice(sides: Literal[4, 6, 8, 10, 12, 20, 100]) -> int:
	'''
	Rolls a die with the specified number of sides and returns the result.

	Args:
		sides (Literal[4, 6, 8, 10, 12, 20, 100]): The number of sides on the die. Must be one of the following: 4, 6, 8, 10, 12, 20, or 100.

	Returns:
		int: The result of the die roll, which will be a random integer between 1 and the number of sides (inclusive).
	'''
	if sides not in [4, 6, 8, 10, 12, 20, 100]:
		raise ValueError("Invalid number of sides. Must be one of the following: 4, 6, 8, 10, 12, 20, or 100.")

	from random import randint
	return randint(1, sides)

def retry_exception(func: Callable[P, R], retries: int = 3, exceptions: tuple = (Exception,), *args: P.args, **kwargs: P.kwargs) -> R:
	'''
	A function that retries a function if it raises an exception.

	Args:
		func (Callable): The function to be decorated.
		retries (int, optional): The number of times to retry the function. Defaults to 3.
		exceptions (tuple[Exception], optional): A tuple of exception classes that should trigger a retry. Defaults to (Exception,).

	Returns:
		Any: The return value of the decorated function if it succeeds within the specified number of retries.
	'''
	for attempt in range(retries):
		try:
			return func(*args, **kwargs)
		except exceptions as e:
			print(f"Attempt {attempt + 1} failed with exception: {e}")
			if attempt < retries - 1:
				continue
			else:
				raise e

def get_chat_model(**kwargs) -> BaseChatModel:
	provider = environ.get('LLM_PROVIDER', '')
	# num_ctx is an Ollama-specific context-window parameter.
	# For OpenAI-compatible providers, map it to max_tokens so callers that
	# rely on it to bound output length still get the intended behaviour.
	num_ctx = kwargs.pop('num_ctx', None)
	if num_ctx is not None and provider != 'ollama':
		kwargs.setdefault('max_tokens', num_ctx)
	elif num_ctx is not None:
		kwargs['num_ctx'] = num_ctx
	# reasoning=False (bool) is an Ollama/Gemini convention; OpenAI-compatible
	# providers expect reasoning to be a dict (reasoning-model config) or absent.
	if isinstance(kwargs.get('reasoning'), bool):
		kwargs.pop('reasoning')
	model = init_chat_model(model=environ.get('LLM_MODEL'), model_provider=provider, **kwargs)
	# transformers serve (and many OpenAI-compatible servers) do not support the
	# response_format JSON-schema mode used by with_structured_output() by default.
	# Patch the method on this instance to always use tool/function calling instead,
	# which these servers do support.
	if provider == 'openai':
		_orig = model.with_structured_output
		def _with_structured_output(schema, **kw):
			kw.setdefault('method', 'function_calling')
			return _orig(schema, **kw)
		model.with_structured_output = _with_structured_output  # type: ignore[method-assign]
	return model