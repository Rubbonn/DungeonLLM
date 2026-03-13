from app.entities.creatures import Player
from langchain_core.messages import BaseMessage
import operator
from typing import TypedDict, Annotated

class State(TypedDict):
	messages: Annotated[list[BaseMessage], operator.add]
	player: Player

def state_to_json(state: State) -> str:
	from app.utilities.jsonable import to_json
	return to_json(state, indent=2)