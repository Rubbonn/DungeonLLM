from dataclasses import fields, is_dataclass
from enum import Enum
import importlib
import json
from langchain_core.load import dumpd, load
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

class CustomDecoder:
	def __call__(self, decoded_dict: dict):
		if 'dungeonllm_class' in decoded_dict:
			class_path = decoded_dict.pop('dungeonllm_class')
			module_name, class_name = class_path.rsplit('.', 1)
			module = importlib.import_module(module_name)
			cls = getattr(module, class_name)
			if hasattr(cls, 'from_dict'):
				return cls.from_dict(decoded_dict)
			return cls(**decoded_dict)
		elif 'lc' in decoded_dict:
			return load(decoded_dict)
		return decoded_dict


def to_json(obj: Any, **kwargs) -> str:
	return json.dumps(obj, cls=CustomEncoder, **kwargs)

def from_json(json_string: str, **kwargs) -> Any:
	if 'object_hook' not in kwargs:
		kwargs['object_hook'] = CustomDecoder()
	return json.loads(json_string, **kwargs)

class Jsonable:
	def __to_dict__(self) -> dict:
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
		from typing import get_type_hints

		data = d.copy()
		data.pop('dungeonllm_class', None)

		if is_dataclass(cls):
			type_hints = get_type_hints(cls)
			for f in fields(cls):
				if f.name in data:
					val = data[f.name]
					field_type = type_hints.get(f.name)
					if isinstance(field_type, type) and issubclass(field_type, Enum):
						if isinstance(val, list):
							data[f.name] = field_type(*val)
						else:
							data[f.name] = field_type(val)
			return cls(**data)

		instance = cls.__new__(cls)
		for k, v in data.items():
			setattr(instance, k, v)
		return instance

	@classmethod
	def from_json(cls, json_string: str) -> 'cls':
		obj = from_json(json_string)
		if not isinstance(obj, cls):
			raise TypeError(f"Expected object of type {cls.__name__}, but got {type(obj).__name__}")
		return obj