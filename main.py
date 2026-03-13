if __name__ == "__main__":
	from app.entities.creatures import Player
	import app.entities.features as features
	from app.graph.build import build_graph
	from app.prompts import SYSTEM_PROMPT, CAMPAIGN_PROMPT
	from app.types.planning import Plan
	from app.types.state import State
	import dotenv
	from langchain.messages import HumanMessage, SystemMessage
	from random import randint

	dotenv.load_dotenv()
	graph = build_graph()
	state: State = {
		'messages': [SystemMessage(content=SYSTEM_PROMPT), HumanMessage(content=CAMPAIGN_PROMPT)],
		'player': Player(name='Ruben', size=features.Size.MEDIUM, abilities={ability.value: features.Ability(ability, randint(5, 15)) for ability in features.AbilityType}),
		'plan': Plan()
	}
	while True:
		state = graph.invoke(state)
		print('----------------------------------')
		print(state['messages'][-1].content)
		print('----------------------------------')

		message = input('> ')
		if message == '/exit':
			break

		state['messages'].append(HumanMessage(content=message))