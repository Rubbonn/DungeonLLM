from app.nodes import nodes, parsers
from app.types.state import SrdParserState
from langgraph.graph import StateGraph, START, END

def build_graph():
	graph_builder = StateGraph(SrdParserState)
	graph_builder.add_node('srd_splitter', nodes.srd_splitter)
	graph_builder.add_node('gear_parser', parsers.gear_parser)
	graph_builder.add_node('damage_types_parser', parsers.damage_types_parser)
	graph_builder.add_node('weapon_properties_parser', parsers.weapon_properties_parser)
	graph_builder.add_node('weapon_mastery_properties_parser', parsers.weapon_mastery_properties_parser)
	graph_builder.add_node('weapons_parser', parsers.weapons_parser)
	graph_builder.add_node('tools_parser', parsers.tools_parser)
	graph_builder.add_edge(START, 'srd_splitter')
	graph_builder.add_edge('srd_splitter', 'gear_parser')
	graph_builder.add_edge('gear_parser', 'tools_parser')
	graph_builder.add_edge('tools_parser', END)
	graph_builder.add_edge('srd_splitter', 'damage_types_parser')
	graph_builder.add_edge('srd_splitter', 'weapon_properties_parser')
	graph_builder.add_edge('srd_splitter', 'weapon_mastery_properties_parser')
	graph_builder.add_edge('damage_types_parser', 'weapons_parser')
	graph_builder.add_edge('weapon_properties_parser', 'weapons_parser')
	graph_builder.add_edge('weapon_mastery_properties_parser', 'weapons_parser')
	graph_builder.add_edge('weapons_parser', END)
	return graph_builder.compile()