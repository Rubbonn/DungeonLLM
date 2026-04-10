if __name__ == "__main__":
	from app.graph.gameplay import build_graph
	from app.prompts import CAMPAIGN_PROMPT
	from app.types.state import GameplayState
	import dotenv
	from langchain.messages import HumanMessage
	from pathlib import Path
	from typing import cast

	dotenv.load_dotenv()

	if not Path('data/databases/entities.sqlite').exists():
		from app.graph.srdparse import build_graph as build_srd_graph
		from app.database import initialize_database
		graph = build_srd_graph()
		initialize_database()
		graph.invoke({'source_file': 'SRD_CC_v5.2.1.md'})

	graph = build_graph()
	from app.test import create_random_player
	state: GameplayState = {
		'messages': [HumanMessage(content=CAMPAIGN_PROMPT)],
		'player': create_random_player(persist=False),
		'plan': None
	}
	while True:
		state = cast(GameplayState, graph.invoke(state))
		print('----------------------------------')
		print(state['messages'][-1].content)
		print('----------------------------------')

		message = input('> ')
		if message == '/exit':
			break

		state['messages'].append(HumanMessage(content=message))