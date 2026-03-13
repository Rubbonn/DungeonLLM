from app.entities.creatures import Player
from app.types.planning import Plan
from langchain_core.messages import BaseMessage
import operator
from typing import TypedDict, Annotated

class State(TypedDict):
	messages: Annotated[list[BaseMessage], operator.add]
	player: Player
	plan: Plan

def state_to_json(state: State) -> str:
	from app.utilities.jsonable import to_json
	return to_json(state, indent=2)