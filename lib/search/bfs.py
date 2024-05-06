"""Implementação da busca em largura."""
from collections import deque

def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    queue = deque([(start, None)])
    visited = {} 
    count_nodes = 0

    while queue:
        vertex, last_vertex = queue.popleft() 
        count_nodes += 1

        if vertex == goal:
            path = [vertex]
            total_cost = 0
            while last_vertex is not None:
                path.append(last_vertex)
                total_cost += graph[last_vertex][1][vertex]
                vertex = last_vertex
                last_vertex = visited.get(vertex)
            path.reverse()
            return (count_nodes, total_cost, path)

        visited[vertex] = last_vertex 

        for next_node, cost in graph[vertex][1].items():
            if next_node not in visited:
                queue.append((next_node, vertex)) 

    return (count_nodes, float('inf'), [])
