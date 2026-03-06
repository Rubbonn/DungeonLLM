from langgraph.graph import StateGraph, START, END
from app.state import State
from app.nodes import queries, commands


def build_graph():
	graph_builder = StateGraph(State)
	graph_builder.add_node('send_message', queries.send_message)
	graph_builder.add_node('route_command', commands.route_command)
	graph_builder.add_node('save_command', commands.save_command)
	graph_builder.add_node('load_command', commands.load_command)
	graph_builder.add_conditional_edges(START, commands.command_or_message, {'message': 'send_message', 'command': 'route_command'})
	graph_builder.add_edge('send_message', END)
	graph_builder.add_edge('save_command', END)
	graph_builder.add_edge('load_command', END)
	return graph_builder.compile()