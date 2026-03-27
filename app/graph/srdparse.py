from app.nodes import nodes, parsers
from app.types.state import SrdParserState
from langgraph.graph import StateGraph, START, END

def build_graph():
	graph_builder = StateGraph(SrdParserState)
	graph_builder.add_node('srd_splitter', nodes.srd_splitter)
	graph_builder.add_node('gear_parser', parsers.gear_parser)
	graph_builder.add_node('weapons_parser', parsers.weapons_parser)
	graph_builder.add_node('tools_parser', parsers.tools_parser)
	graph_builder.add_edge(START, 'srd_splitter')
	graph_builder.add_edge('srd_splitter', 'gear_parser')
	graph_builder.add_edge('gear_parser', 'weapons_parser')
	graph_builder.add_edge('weapons_parser', 'tools_parser')
	graph_builder.add_edge('tools_parser', END)
	return graph_builder.compile()