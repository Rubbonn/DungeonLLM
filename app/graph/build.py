from langgraph.graph import StateGraph, START, END
from app.state import State
from app import nodes


def build_graph():
	graph_builder = StateGraph(State)
	graph_builder.add_node('send_message', nodes.send_message)
	graph_builder.add_edge(START, 'send_message')
	graph_builder.add_edge('send_message', END)
	return graph_builder.compile()