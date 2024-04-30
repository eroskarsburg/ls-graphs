"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""
from heapq import heapify, heappush, heappop
from typing import List, Tuple
from graph import Graph

# Implementação do algoritmo de Dijkstra
def dijkstra(graph: Graph, start: int, goal: int) -> Tuple[int, float, List[int]]:
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""
    num_nodes_explored = 0
    path_length = 0
    path = []

    # Dicionário para manter o custo atual do caminho do nó inicial até cada nó
    distances = {node: float('inf') for node in range(graph.num_nodes)}
    distances[start] = 0

    # Dicionário para manter o nó anterior no caminho mais curto até cada nó
    previous = {}

    # Conjunto de nós não visitados
    unvisited = set(range(graph.num_nodes))

    # Loop principal do algoritmo
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        num_nodes_explored += 1

        if current == goal:
            # Reconstrói o caminho
            while current in previous:
                path.insert(0, current)
                current = previous[current]
            path.insert(0, start)
            path_length = distances[goal]
            return num_nodes_explored, path_length, path

        unvisited.remove(current)

        for neighbor, cost in graph.adjacency_list[current]:
            new_distance = distances[current] + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

    return num_nodes_explored, path_length, path