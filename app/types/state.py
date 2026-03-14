from app.entities.creatures import Player
from app.types.planning import Plan
from langchain.messages import AnyMessage
from typing import TypedDict

class State(TypedDict):
	messages: list[AnyMessage]
	player: Player
	plan: Plan | None

def state_to_json(state: State) -> str:
	from app.utilities.jsonable import to_json
	return to_json(state, indent=2)