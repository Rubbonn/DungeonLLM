if __name__ == "__main__":
	from app.entities.creatures import Player
	import app.entities.features as features
	from app.graph.gameplay import build_graph
	from app.prompts import CAMPAIGN_PROMPT
	from app.types.state import GameplayState
	import dotenv
	from langchain.messages import HumanMessage
	from random import randint
	from typing import cast

	from app.graph.srdparse import build_graph as build_srd_graph
	from app.database import initialize_database
	import sys
	graph = build_srd_graph()
	initialize_database()
	graph.invoke({'source_file': 'SRD_CC_v5.2.1.md'})
	sys.exit(0)

	dotenv.load_dotenv()
	graph = build_graph()
	state: GameplayState = {
		'messages': [HumanMessage(content=CAMPAIGN_PROMPT)],
		'player': Player(name='Ruben', size=features.Size.MEDIUM, abilities={ability: features.Ability(ability, randint(5, 15)) for ability in features.AbilityType}),
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