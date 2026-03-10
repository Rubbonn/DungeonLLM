from enum import Enum
import json
from langchain_core.load.dump import dumpd
from langchain_core.load.serializable import Serializable
from typing import Any


class CustomEncoder(json.JSONEncoder):
	def default(self, o):
		if hasattr(o, '__to_dict__'):
			return o.__to_dict__()
		elif isinstance(o, Serializable):
			return dumpd(o)
		elif isinstance(o, Enum):
			return o.value
		return super().default(o)

def to_json(obj: Any, **kwargs) -> str:
	return json.dumps(obj, cls=CustomEncoder, **kwargs)

class Jsonable:
	def __to_dict__(self) -> dict:
		from dataclasses import asdict, fields, is_dataclass
		if is_dataclass(self):
			return {
				**{f.name: getattr(self, f.name) for f in fields(self)},
				'dungeonllm_class': f'{self.__class__.__module__}.{self.__class__.__name__}'
			}
		properties = {k: v for k, v in vars(self).items() if not k.startswith('_')}
		properties['dungeonllm_class'] = f'{self.__class__.__module__}.{self.__class__.__name__}'
		return properties

	def to_dict(self) -> dict:
		return self.__to_dict__()

	def to_json(self) -> str:
		return to_json(self)

	@classmethod
	def from_dict(cls, d: dict) -> 'cls':
		pass

	@classmethod
	def from_json(cls, json_string: str) -> 'cls':
		pass