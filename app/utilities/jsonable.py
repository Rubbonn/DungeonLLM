from enum import Enum
import json
from langchain_core.load.dump import dumpd
from langchain_core.load.serializable import Serializable


class CustomEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, Jsonable):
			return o.to_dict()
		elif isinstance(o, Serializable):
			return dumpd(o)
		elif isinstance(o, Enum):
			return o.value
		return super().default(o)

class Jsonable:
	def to_dict(self) -> dict:
		properties = {prop: getattr(self, prop) for prop in dir(self) if not prop.startswith('_') and not callable(getattr(self, prop))}
		properties['dungeonllm_class'] = f'{self.__class__.__module__}.{self.__class__.__name__}'
		return properties

	def to_json(self) -> str:
		return json.dumps(self, cls=CustomEncoder)

	@classmethod
	def from_dict(cls, d: dict) -> 'cls':
		pass

	@classmethod
	def from_json(cls, json_string: str) -> 'cls':
		pass