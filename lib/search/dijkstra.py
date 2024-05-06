
"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""
    distances = {vertex: float('inf') for vertex in range(len(graph))}
    distances[start] = 0
    path = []
    priority_queue = [(start, 0)]
    prev = {}
    while priority_queue:
        vertex, current_dist = min(priority_queue)
        if vertex == goal:
            break
        priority_queue.remove((vertex, current_dist))
        for nbor_vertex in graph[vertex][1]:
            nbor_dist = graph[vertex][1][nbor_vertex]
            new_dist = current_dist + nbor_dist
            if new_dist < distances[nbor_vertex]:
                distances[nbor_vertex] = new_dist
                prev[nbor_vertex] = vertex
                priority_queue.append((nbor_vertex, new_dist))
    vertex = goal
    while vertex != start:
        path.append(vertex)
        vertex = prev[vertex]
    path.append(start)
    path.reverse()

    return len(path), distances[goal], path