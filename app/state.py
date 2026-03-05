from langchain_core.messages import BaseMessage
import operator
from typing import TypedDict, Annotated

class State(TypedDict):
	messages: Annotated[list[BaseMessage], operator.add]