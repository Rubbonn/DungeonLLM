if __name__ == "__main__":
	from app.graph.build import build_graph
	from app.state import State
	import dotenv
	from langchain.messages import HumanMessage, SystemMessage

	dotenv.load_dotenv()
	graph = build_graph()
	state: State = {'messages': [SystemMessage(content='You are a bad assistant that always responds with a sarcastic tone.')]}
	while True:
		message = input('> ')
		if message == 'exit':
			break

		state['messages'].append(HumanMessage(content=message))
		state = graph.invoke(state)
		print(state['messages'][-1].content)