from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.embeddings import Embeddings
from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings
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
	return init_chat_model(model=environ.get('LLM_MODEL'), model_provider=environ.get('LLM_PROVIDER'), **kwargs)

def get_embedding_model(**kwargs) -> Embeddings:
	return init_embeddings(model=environ.get('LLM_EMBEDDING_MODEL'), provider=environ.get('LLM_PROVIDER'), **kwargs)

def get_vector_store():
	from langchain_chroma import Chroma
	return Chroma(collection_name='dungeon_srd', embedding_function=get_embedding_model(), persist_directory='data/databases/vectorstore')