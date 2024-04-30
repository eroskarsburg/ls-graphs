"""Implementação do algoritmo 'branch and bound'."""
from graph import Graph
from typing import List, Tuple

def branch_and_bound(graph: Graph, start: int, goal: int) -> Tuple[int, float, List[int]]:
    """Busca um caminho entre start e goal usando Branch and Bound."""
    num_nodes_explored = 0
    shortest_path_length = float('inf')
    shortest_path = []

    def branch_and_bound_helper(current_node: int, path: List[int], path_length: float):
        nonlocal num_nodes_explored, shortest_path_length, shortest_path
        num_nodes_explored += 1

        if current_node == goal:
            if path_length < shortest_path_length:
                shortest_path_length = path_length
                shortest_path = path.copy()
            return

        for neighbor, cost in graph.adjacency_list[current_node]:
            if neighbor not in path:
                if path_length + cost < shortest_path_length:
                    branch_and_bound_helper(neighbor, path + [neighbor], path_length + cost)

    branch_and_bound_helper(start, [start], 0)

    return num_nodes_explored, shortest_path_length, shortest_path