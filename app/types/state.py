from app.entities.creatures import Player
from app.types.planning import Plan
from langchain_core.messages import BaseMessage
from typing import TypedDict

class State(TypedDict):
	messages: list[BaseMessage]
	player: Player
	plan: Plan | None

def state_to_json(state: State) -> str:
	from app.utilities.jsonable import to_json
	return to_json(state, indent=2)