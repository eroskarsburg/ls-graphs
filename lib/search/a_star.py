"""Implementação do algoritmo A*."""
from queue import PriorityQueue
from util import heuristic

def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    const_so_far = {}
    came_from[start] = None
    const_so_far[start] = 0
    while not frontier.empty():
        vertex = frontier.get()
        if vertex == goal:
            break
        for nbor_vertex in graph[vertex][1]:
            nbor_dist = graph[vertex][1][nbor_vertex]
            new_cost = const_so_far[vertex] + nbor_dist
            if nbor_vertex not in const_so_far or new_cost < const_so_far[nbor_vertex]:
                const_so_far[nbor_vertex] = new_cost
                priority = new_cost + heuristic(graph[nbor_vertex], graph[goal])
                frontier.put(nbor_vertex, priority)
                came_from[nbor_vertex] = vertex
    predecessor = came_from[vertex]
    path = [vertex]
    while predecessor != None:
        path.append(predecessor)
        predecessor = came_from[predecessor]
    path.reverse()
    return (len(path) + 1, const_so_far[goal], path)
