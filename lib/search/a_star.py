"""Implementação do algoritmo A*."""
from heapq import heappush, heappop
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
        current = frontier.get()
        if current == goal:
            predecessor = came_from[current]
            path = [current]
            while predecessor != None:
                path.append(predecessor)
                predecessor = came_from[predecessor]
            path.reverse()
            break
        for next_node, next_node_cost in graph[current][1]:
            new_cost = const_so_far[current] + next_node_cost
            if next_node not in const_so_far or new_cost < const_so_far[next_node]:
                const_so_far[next_node] = new_cost
                priority = new_cost + heuristic(graph[next_node], graph[goal])
                frontier.put(next_node, priority)
                came_from[next_node] = current
    return (len(path) - 1, const_so_far[goal], path)
