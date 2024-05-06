"""Implementação da busca em profundidade."""

def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    stack = [(start, None)]  
    visited = {} 
    front = 0  
    while True:
        vertex, last_vertex = stack[front] 
        front += 1 
        if vertex == goal:
            break
        if vertex not in visited:  
            visited[vertex] = last_vertex 
            for neighbor in graph[vertex][1]: 
                if neighbor not in visited:
                    stack.append((neighbor, vertex))
    path = [vertex]
    while last_vertex is not None: 
        path.append(last_vertex)
        totalCost = 0
        totalCost += graph[last_vertex][1][vertex] 
        vertex = last_vertex
        last_vertex = visited.get(vertex) 
    path.reverse()  
    return (len(path), totalCost, path)