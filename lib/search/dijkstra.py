from heapq import heappop, heappush

def makeDict(graph):
    """usada no dijkstra para criar um dicionário com os pontos do grafo e seus visinhos e custos"""
    dict = {}
    for ponto in range(len(graph)):
        dictVisinhos = {}
        for visinho in graph[ponto][1]:
            dictVisinhos[visinho[0]] = visinho[1]
        x = float(graph[ponto][0][0])
        y = float(graph[ponto][0][1])
        dict[ponto] = {
            "posicao": {"x": x, "y": y},
            "visinhos": dictVisinhos,
            "custo": 0,
            "anteriores": [],
        }
    return dict


def dijkstra(graph, start: int, goal: int):
    grafo_dicionario = makeDict(graph)
    grafo_dicionario[start]["custo"] = 0
    visitados = set()
    heap = [(0, start)]

    while heap:  # enquanto heap não estiver vazio
        cost, current_node = heappop(heap)
        if current_node in visitados:
            continue
        visitados.add(current_node)

        if current_node == goal:
            shortest_path = reconstruir_path(grafo_dicionario, start, goal)
            return len(visitados), cost, shortest_path

        for visinho, distancia_visinho in grafo_dicionario[current_node][
            "visinhos"
        ].items():
            if visinho not in visitados:
                custo_total = cost + distancia_visinho
                if custo_total < grafo_dicionario[visinho]["custo"]:
                    grafo_dicionario[visinho]["custo"] = custo_total
                    grafo_dicionario[visinho]["anteriores"] = [current_node]
                    heappush(heap, (custo_total, visinho))
                elif custo_total == grafo_dicionario[visinho]["custo"]:
                    grafo_dicionario[visinho]["anteriores"].append(current_node)

    return len(visitados), float("inf"), []


def reconstruir_path(graph, start, goal):
    path = [goal]
    while path[-1] != start:
        current = path[-1]
        previouscurrent_nodes = graph[current]["anteriores"]
        if not previouscurrent_nodes:
            return []  # no path
        path.append(previouscurrent_nodes[0])
    return list(reversed(path))
