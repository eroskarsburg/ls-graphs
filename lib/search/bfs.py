"""Implementação da busca em largura."""
from queue import deque as Queue

def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    try:
        graph[start]
        graph[goal]
    except KeyError:
        print("Node doesn't exist")
        return None

    stack = [(start, None)]  
    visitedNodes = {} 
    front = 0  
    while front < len(stack):
        v, predecessor = stack[front] 
        front += 1 

        if v == goal:  
            path = [v]  
            totalCost = 0  
            countNodes = 1  
            while predecessor is not None: 
                path.append(predecessor)
                totalCost += graph[predecessor][1][v] 
                v = predecessor
                predecessor = visitedNodes.get(v) 
                countNodes += 1 
            path.reverse()  
            return (countNodes, totalCost, path)

        if v not in visitedNodes:  
            visitedNodes[v] = predecessor 
            for neighbor, cost in graph[v][1].items(): 
                if neighbor not in visitedNodes:  
                    stack.append((neighbor, v)) 

    print("Goal not reachable")
    return None
