from app.entities.creatures import Player
from app.types.planning import Plan
from langchain.messages import AnyMessage
from typing import TypedDict

class GameplayState(TypedDict):
	messages: list[AnyMessage]
	player: Player
	plan: Plan | None

class SrdParserState(TypedDict):
	source_file: str
	sections: list[str]

def state_to_json(state: GameplayState) -> str:
	from app.utilities.jsonable import to_json
	return to_json(state, indent=2)