from queue import PriorityQueue

def dijkstra(graph, start, goal):
    distances = {vertex: float('inf') for vertex in range(len(graph))}
    distances[start] = 0
    path = []
    priority_queue = [(0, start)]
    predecessors = {}
    while priority_queue:
        current_distance, current_vertex = min(priority_queue)
        if current_vertex == goal:
            break
        priority_queue.remove((current_distance, current_vertex))
        for neighbor, weight in graph[current_vertex][1]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                priority_queue.append((distance, neighbor))
    current_vertex = goal
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = predecessors[current_vertex]
    path.append(start)
    path.reverse()

    return distances[goal], path