from langchain_core.messages import BaseMessage
from langchain.messages import SystemMessage
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.types import Overwrite
from operator import add

class State(TypedDict):
	messages: Annotated[list[BaseMessage], add]

graph_builder = StateGraph(State)

def add_system_prompt(state: State):
	return {'messages': Overwrite([SystemMessage(content='You are a bad assistant that always responds with a sarcastic tone.')] + state['messages'])}

def send_message(state: State):
	chat_model = init_chat_model(model='qwen/qwen3.5-397b-a17b', model_provider='nvidia')
	response = chat_model.invoke(state['messages'])
	return {'messages': [response]}

graph_builder.add_node('add_system_prompt', add_system_prompt)
graph_builder.add_node('send_message', send_message)
graph_builder.add_edge(START, 'add_system_prompt')
graph_builder.add_edge('add_system_prompt', 'send_message')
graph_builder.add_edge('send_message', END)
graph = graph_builder.compile()

if __name__ == "__main__":
	import dotenv
	from langchain.chat_models import init_chat_model

	dotenv.load_dotenv()
	message = input('> ')
	response = graph.invoke({'messages': [{'role': 'user', 'content': message}]})
	print(response['messages'][-1].content)