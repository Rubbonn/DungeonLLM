from app.types.state import State
from langgraph.types import Overwrite

def help_command(state: State) -> None:
	print('Comandi disponibili:')
	print('/save - Salva la campagna')
	print('/load - Carica la campagna')
	print('/exit - Esci dal programma')
	print('/help - Mostra questo messaggio')

def save_command(state: State) -> None:
	from app.types.state import state_to_json
	with open('data/saves/campaign.json', 'w') as f:
		f.write(state_to_json(state))
	print('Campagna salvata!')

def load_command(state: State) -> State:
	from app.utilities.jsonable import from_json
	with open('data/saves/campaign.json', 'r') as f:
		state = {k: Overwrite(v) for k,v in from_json(f.read()).items()}
	print('Campagna caricata!')
	return state