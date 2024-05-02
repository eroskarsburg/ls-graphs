"""Implementação do algoritmo 'branch and bound'."""

from typing import List, Tuple

def branch_and_bound(graph, start: int, goal: int) -> Tuple[int, float, List[int]]:
    """Busca um caminho entre start e goal usando Branch and Bound."""
    visited = set() # Uma lista contendo os nodos já visitados.
    stack = [(0, 0, [start])]  # (lower_bound, cost, path).
    best = []

    while stack:
        stack.sort()  # Ordena a pilha com base no lower_bound.
        lb, cost, current_path = stack.pop(0) # Atribui os valores inicias e remove o primeiro elemento da stack.
        node = current_path[-1] # Atribui a "node" o valor do último elemento no path da lista.

        if node == goal: # Testa se o nodo é o goal.
            if not best: # Testa se o novo caminho é menos custoso que o já encontrado.
                best.append((len(visited), cost, current_path)) # Atribui o caminho recém encontrado como o melhor.
            elif best and best[0][1] > cost:
                best[0] = (len(visited), cost, current_path)

        if node not in visited:
            visited.add(node)
            neighbors = graph[node][1]
            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    if not best or (best and cost + edge_cost < best[0][1]):
                        new_cost = cost + edge_cost
                        new_path = current_path + [neighbor]
                        new_lb = new_cost  # No Branch and Bound puro, não usamos heurística
                        stack.append((new_lb, new_cost, new_path))

    return best or "Nenhum caminho foi encontrado!"



# def branch_and_bound(Grafo, start, goal):
#     assert(start in Grafo.vertices)
#     assert(goal in Grafo.vertices)
#     best_so_far = (None, math.inf)
#     Q = Queue()
#     Q.enqueue(start)
#     while not Q.is_empty():
#         v = Q.dequeue()
#         if goal == v:
#             # 'candidate' é o comprimento atual do caminho
#             new_path, candidate = processa_caminho(v)
#             path, limit = best_so_far
#             if candidate < limit:
#                 best_so_far = (new_path, candidate)
#         else:
#             ajusta_caminho(start, v)
#             for u in Grafo.neighbors(v):
#                 # Só adiciona caminhos que podem ser melhores
#                 if caminho_ate_aqui(start, u) < best_so_far:
#                     Q.enqueue(u)