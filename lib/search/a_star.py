"""Implementação do algoritmo A*."""
from typing import List, Tuple
from graph import Graph

# Função para calcular a distância (heurística) entre dois nós usando a distância euclidiana
def euclidean_distance(node1_coords: Tuple[float, float], node2_coords: Tuple[float, float]) -> float:
    return ((node1_coords[0] - node2_coords[0]) ** 2 + (node1_coords[1] - node2_coords[1]) ** 2) ** 0.5


def a_star(graph: Graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""
    num_nodes_explored = 0
    path_length = 0
    path = []

    # Função de heurística (distância euclidiana)
    def heuristic(node: int) -> float:
        return euclidean_distance(graph.coordinates[node], graph.coordinates[goal])

    # Inicialização da fila de prioridade (open set) com o nó inicial
    open_set = [(start, 0 + heuristic(start))]
    came_from = {}

    # Dicionário para manter o custo atual do caminho do nó inicial até cada nó
    g_score = {node: float('inf') for node in range(graph.num_nodes)}
    g_score[start] = 0

    # Loop principal do algoritmo
    while open_set:
        current, _ = min(open_set, key=lambda x: x[1])  # Seleciona o nó com menor f(x)
        num_nodes_explored += 1

        if current == goal:
            # Reconstrói o caminho
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return num_nodes_explored, g_score[goal], path

        open_set.remove((current, g_score[current] + heuristic(current)))  # Remove o nó da fila de prioridade

        for neighbor, cost in graph.adjacency_list[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                open_set.append((neighbor, tentative_g_score + heuristic(neighbor)))  # Adiciona o vizinho à fila de prioridade

    return num_nodes_explored, path_length, path