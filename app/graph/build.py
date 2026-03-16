from app.nodes import nodes, commands, routers
from app.types.state import State
from langgraph.graph import StateGraph, START, END


def build_graph():
	graph_builder = StateGraph(State)
	graph_builder.add_node('planner', nodes.planner)
	graph_builder.add_node('executor', nodes.executor)
	graph_builder.add_node('send_message', nodes.send_message)
	graph_builder.add_node('route_command', routers.route_command)
	graph_builder.add_node('save_command', commands.save_command)
	graph_builder.add_node('load_command', commands.load_command)
	graph_builder.add_node('help_command', commands.help_command)
	graph_builder.add_conditional_edges(START, routers.command_or_message, {'message': 'planner', 'command': 'route_command'})
	graph_builder.add_edge('planner', 'executor')
	graph_builder.add_edge('executor', 'send_message')
	graph_builder.add_edge('send_message', END)
	graph_builder.add_edge('save_command', END)
	graph_builder.add_edge('help_command', END)
	graph_builder.add_edge('load_command', END)
	return graph_builder.compile()