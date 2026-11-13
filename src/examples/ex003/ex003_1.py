from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, add_messages
from rich import print
import operator

# 1 - Definir estado
class State(TypedDict):
    nodes_path: Annotated[list[str], operator.add]
    
# 2 - Definir nodes
def node_a(state: State) -> State:
    nodes_path = state['nodes_path']
    output_state: State = {'nodes_path': ["A"]}
    print("> node_a", f"{state}", f"{output_state=}")
    return output_state


def node_b(state: State) -> State:
    nodes_path = state['nodes_path']
    output_state: State = {'nodes_path': ["B"]}
    print("> node_b", f"{state}", f"{output_state=}")
    return output_state

    
# Definir builder
builder = StateGraph(State)

builder.add_node('A', node_a)
builder.add_node('B', node_b)

# Conectar as Edges
builder.add_edge('__start__', 'A')
builder.add_edge('A', 'B')
builder.add_edge('B', '__end__')

# Compilar grafo
graph = builder.compile()

response = graph.invoke({"nodes_path": []})

# Resultado de todo o grafo
print()
print(f"{response}")
print()

# Visualização do grafo
# graph.get_graph().draw_mermaid_png(output_file_path="file.png")
# print(graph.get_graph().draw_mermaid())