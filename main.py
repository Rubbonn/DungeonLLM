if __name__ == "__main__":
	from app.graph.build import build_graph
	from app.prompts import SYSTEM_PROMPT, CAMPAIGN_PROMPT
	from app.state import State
	import dotenv
	from langchain.messages import HumanMessage, SystemMessage

	dotenv.load_dotenv()
	graph = build_graph()
	state: State = {'messages': [SystemMessage(content=SYSTEM_PROMPT), HumanMessage(content=CAMPAIGN_PROMPT)]}
	while True:
		state = graph.invoke(state)
		print('----------------------------------')
		print(state['messages'][-1].content)
		print('----------------------------------')

		message = input('> ')
		if message == 'exit':
			break

		state['messages'].append(HumanMessage(content=message))