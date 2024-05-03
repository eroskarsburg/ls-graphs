
"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

from heapq import heapify, heappush, heappop

def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""
    distances = {vertex: float('inf') for vertex in range(len(graph))}
    distances[start] = 0
    path = []
    priority_queue = [(start, 0)]
    prev = {}
    while priority_queue:
        current_vertex, current_dist = min(priority_queue)
        if current_vertex == goal:
            break
        priority_queue.remove((current_vertex, current_dist))
        for nbor_vertex, nbor_dist in graph[current_vertex][1]:
            new_dist = current_dist + nbor_dist
            if new_dist < distances[nbor_vertex]:
                distances[nbor_vertex] = new_dist
                prev[nbor_vertex] = current_vertex
                priority_queue.append((nbor_vertex, new_dist))
    current_vertex = goal
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = prev[current_vertex]
    path.append(start)
    path.reverse()

    return len(path), distances[goal], path