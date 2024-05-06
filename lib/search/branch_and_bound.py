"""Implementação do algoritmo 'branch and bound'."""

from typing import List, Tuple

def branch_and_bound(graph, start: int, goal: int) -> Tuple[int, float, List[int]]:
    """Busca um caminho entre start e goal usando Branch and Bound."""
    queue = [(start, None)]
    visited = {} 
    best_path = None
    best_cost = float('inf')
    count_vertex, path = 0, []

    while len(queue):
        vertex, last_vertex = queue.pop(0)

        if goal == vertex:
            path = [vertex]
            totalCost = 0

            while last_vertex is not None: 
                path.append(last_vertex)
                totalCost += graph[last_vertex][1][vertex]
                vertex = last_vertex
                last_vertex = visited.get(vertex) 

            path.reverse()
            if totalCost < best_cost:
                best_path = path
                best_cost = totalCost
            continue

        if vertex not in visited:
            count_vertex += 1
            visited[vertex] = last_vertex 

            for neighbor in graph[vertex][1]:
                cost = graph[vertex][1][neighbor]
                if neighbor not in visited and cost < best_cost:
                    queue.append((neighbor, vertex))

    if best_path is not None:
        return (count_vertex, best_cost, best_path)