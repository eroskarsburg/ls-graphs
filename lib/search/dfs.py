"""Implementação da busca em profundidade."""
from heapq import heapify, heappush, heappop

def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    stack = [start, 0]
    visNodes = []
    while len(stack):
        v = stack.pop()
        if goal == v[0]:
            predVert = v[1]
            path = [ v[0], predVert ]
            totalCost = v[2]
            countNodes = 1
            if predVert != start:
                countNodes += 1
            while len(visNodes):
                temp = visNodes.pop()
                if predVert == temp[0]:
                    predVert = temp[1]
                    if predVert != None:
                        totalCost += temp[2]
                        path.append(predVert)
                        if predVert != start:
                            countNodes += 1
            path.reverse()
            return (countNodes, totalCost, path)
        if not v in visNodes:
            visNodes.append(v)               
            for key, value in graph[v[0]][1].items():
                stack.append( (key, v[0], value) )