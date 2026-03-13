from app.types.state import State
from langgraph.types import Command
from typing import Literal

def command_or_message(state: State) -> str:
	return 'command' if state['messages'][-1].content.startswith('/') else 'message'

def must_execute_tool_calls(state: State) -> bool:
	return len(state['messages'][-1].tool_calls) > 0

def route_command(state: State) -> Command[Literal['save_command', 'load_command', 'help_command']]:
	command = state['messages'][-1].content[1:]
	del state['messages'][-1]
	return Command(goto=f'{command}_command')