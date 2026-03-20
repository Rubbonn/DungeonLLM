from app.nodes import nodes
from app.types.state import SrdParserState
from langgraph.graph import StateGraph, START, END

def build_graph():
	graph_builder = StateGraph(SrdParserState)
	graph_builder.add_node('srd_splitter', nodes.srd_splitter)
	graph_builder.add_node('gear_parser', nodes.gear_parser)
	graph_builder.add_edge(START, 'srd_splitter')
	graph_builder.add_edge('srd_splitter', 'gear_parser')
	graph_builder.add_edge('gear_parser', END)
	return graph_builder.compile()