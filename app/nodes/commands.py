from app.state import State
from langgraph.types import Command, Overwrite
from typing import Literal

def command_or_message(state: State) -> str:
	return 'command' if state['messages'][-1].content.startswith('/') else 'message'

def route_command(state: State) -> Command[Literal['save_command']]:
	command = state['messages'][-1].content[1:]
	del state['messages'][-1]
	return Command(goto=f'{command}_command')

def save_command(state: State) -> None:
	from langchain_core.load.dump import dumps
	with open('data/saves/campaign.json', 'w') as f:
		f.write(dumps(state, pretty=True, indent=4))
	print('Campagna salvata!')

def load_command(state: State) -> State:
	from langchain_core.load.load import loads
	with open('data/saves/campaign.json', 'r') as f:
		state = {k: Overwrite(v) for k,v in loads(f.read()).items()}
	print('Campagna caricata!')
	return state