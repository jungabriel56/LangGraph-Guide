from typing import TypedDict

from langgraph.graph import StateGraph

# 1 - Definir estado
class State(TypedDict):
    nodes_path: list[str]
    
# 2 - Definir nodes
def node_a(state: State) -> None:
    pass


def node_b(state: State) -> None:
    pass
    

# Definir builder
builder = StateGraph(State)

builder.add_node('A', node_a)
builder.add_node('B', node_b)

# Conectar as Edges
builder.add_edge('__start__', 'A')
builder.add_edge('A', 'B')
builder.add_edge('B', '__end__')

graph = builder.compile()

graph.get_graph().draw_mermaid_png(output_file_path="file.png")