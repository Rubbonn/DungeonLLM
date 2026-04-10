from app.nodes import nodes, parsers
from app.types.state import SrdParserState
from langgraph.graph import StateGraph, START, END

def build_graph():
	graph_builder = StateGraph(SrdParserState)
	graph_builder.add_node('srd_splitter', nodes.srd_splitter)
	graph_builder.add_node('delete_srd_splitted_files', nodes.delete_srd_splitted_files, defer=True)
	graph_builder.add_node('srd_embedder', nodes.srd_embedder)
	graph_builder.add_node('gear_parser', parsers.gear_parser)
	graph_builder.add_node('weapons_parser', parsers.weapons_parser)
	graph_builder.add_node('tools_parser', parsers.tools_parser)
	graph_builder.add_node('animals_parser', parsers.animals_parser)
	graph_builder.add_node('armors_parser', parsers.armors_parser)
	graph_builder.add_edge(START, 'srd_splitter')
	graph_builder.add_edge('srd_splitter', 'gear_parser')
	graph_builder.add_edge('gear_parser', 'tools_parser')
	graph_builder.add_edge('tools_parser', 'delete_srd_splitted_files')
	graph_builder.add_edge('srd_splitter', 'weapons_parser')
	graph_builder.add_edge('weapons_parser', 'delete_srd_splitted_files')
	graph_builder.add_edge('srd_splitter', 'animals_parser')
	graph_builder.add_edge('animals_parser', 'delete_srd_splitted_files')
	graph_builder.add_edge('srd_splitter', 'armors_parser')
	graph_builder.add_edge('armors_parser', 'delete_srd_splitted_files')
	graph_builder.add_edge('delete_srd_splitted_files', 'srd_embedder')
	graph_builder.add_edge('srd_embedder', END)
	return graph_builder.compile()