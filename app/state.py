from app.entities.creatures import Player
from app.utilities.jsonable import CustomEncoder
from json import dumps
from langchain_core.messages import BaseMessage
import operator
from typing import TypedDict, Annotated

class State(TypedDict):
	messages: Annotated[list[BaseMessage], operator.add]
	player: Player

def state_to_json(state: State) -> str:
	return dumps(state, cls=CustomEncoder, indent=2)