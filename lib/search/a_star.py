import heapq
import math
from typing import Tuple

class priorityQueue:
    def __init__(self):
        self.cities = []
    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
    def pop(self):
        return heapq.heappop(self.cities)[1]
    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False
    def check(self):
        print(self.cities)

class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

romania = {}


class Diction():

    def __init__(self, coordX = 0, coordY = 0, cost = 0, neighbors = {}, last_neighb = {}):
        self.coordX = coordX
        self.coordY = coordY
        self.posicao_coords = [coordX, coordY]
        self.cost = cost
        self.neighbors = neighbors
        self.last_neighb = last_neighb

    def dictMaker(self, graph):
        dic = {}
        for index in range(len(graph)):
            d_neighbors = {}
            for neigh in graph[index][1]:
                d_neighbors[neigh[0]] = neigh[1]
            self.coordX = (graph[index][1][0])
            self.coordY = (graph[index][1][1])
            self.posicao_coords = [self.coordX, self.coordY]
            dic[index] = {
                "posicao": {"x": self.coordX, "y": self.coordY},
                "visinhos": d_neighbors,
                "custo": 0,
                "anteriores": [],
            }
        return dic


def dict_maker(graph):
    dict = {}
    for ponto in range(len(graph)):
        dictVisinhos = {}
        for visinho in graph[ponto][1]:
            dictVisinhos[visinho[0]] = visinho[1]
        x = float(graph[ponto][0][0])
        y = float(graph[ponto][0][1])
        dict[ponto] = {
            "coordinates": {"x": x, "y": y},
            "neighbors": dictVisinhos,
            "cost": 0,
            "visited_neighbors": [],
        }
    return dict


def haversine(lat1, lon1, lat2, lon2):
    """Calcula a distância, em metros, entre duas coordenadas GPS."""
    dLat = (lat2 - lat1) * math.pi / 180.0  # pylint: disable=invalid-name
    dLon = (lon2 - lon1) * math.pi / 180.0  # pylint: disable=invalid-name
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
    # apply formulae
    a = pow(math.sin(dLat / 2), 2) + pow(math.sin(dLon / 2), 2) * math.cos(
        lat1
    ) * math.cos(lat2)
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return (rad * c) * 1000



def makeDict2(graph, goal):
    dict = {}
    goalPos = graph[goal][0]
    for ponto in range(len(graph)):
        dictVisinhos = {}
        for visinho in graph[ponto][1]:
            dictVisinhos[visinho[0]] = visinho[1]
        x = float(graph[ponto][0][0])
        y = float(graph[ponto][0][1])
        dict[ponto] = {
            "posicao": {"x": x, "y": y},
            "visinhos": dictVisinhos,
            "custo": float("inf"),
            "anteriores": [],
            "goalDistance": 0,
        }
    return dict


def a_star2(graph, start, goal):
    grafo_dicionario = makeDict2(graph, goal)
    grafo_dicionario[start]["custo"] = 0
    visitados = set()
    heap = [(0, start)]
    current_node = 0

    while heap:
        current_node = heapq.heappop(heap)[1]
        if current_node in visitados:
            continue
        visitados.add(current_node)
        if current_node == goal:
            break
        for visinho in grafo_dicionario[current_node]["visinhos"]:

            new_cost = (
                grafo_dicionario[current_node]["custo"]
                + grafo_dicionario[current_node]["visinhos"][visinho]
            )
            if new_cost < grafo_dicionario[visinho]["custo"] and visinho not in visitados:
                print(visinho)
                grafo_dicionario[visinho][
                    "custo"
                ] = new_cost
                priority = new_cost + haversine(
                    grafo_dicionario[goal]["posicao"]["x"],
                    grafo_dicionario[goal]["posicao"]["y"],
                    grafo_dicionario[visinho]["posicao"]["x"],
                    grafo_dicionario[visinho]["posicao"]["y"],
                )
                heapq.heappush(heap, (priority, visinho))
                grafo_dicionario[visinho][
                    "anteriores"
                ] = current_node
    path = []
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = grafo_dicionario[current_node]["anteriores"]
    path.append(start)
    path.reverse()
    return len(visitados), grafo_dicionario[goal]["custo"], path


def a_star(graph, start, goal):
    dict = dict_maker(graph)
    start_node = dict[start]
    goal_node = dict[goal]
    closed_list = set()
    opened_list = set()
    g = 0 # custo do node atual até o node final
    h = 0 # custo do node atual até o node inicial
    best_cost = 10000000
    heap = [(0, start)]

    while heap:
        cur_node = heapq.heappop(heap)[1]
        if cur_node in closed_list:
            continue
        opened_list.add(cur_node)
        for current_neighbor in dict[cur_node]['neighbors'].items():
            opened_list.add(current_neighbor)
        for item in opened_list:
            cost = item[1]
            if cost < best_cost:
                best_cost = cost
                closed_list.add(cur_node)

        opened_list.remove(cur_node)



    return None



def heuristic(node, goal_node):
    x1, y1 = node
    x2, y2 = goal_node
    val = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return val  # Euclidean distance


# Example usage
def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    with open(filename, "rt") as input_file:
        vertex_count = int(input_file.readline().strip())
        graph = [[] for _ in range(vertex_count)]

        for _ in range(vertex_count):
            index, latitude, longitude = input_file.readline().strip().split()
            graph[_].append((latitude, longitude))  # vertex
            graph[_].append([])  # edges

        for _ in range(int(input_file.readline().strip())):
            from_vertex, to_vertex, cost = input_file.readline().strip().split()
            graph[int(from_vertex)][1].append([int(to_vertex), float(cost)])
            graph[int(to_vertex)][1].append([int(from_vertex), float(cost)])
    return graph


graph = read_graph("lib\mapas\mini_map.txt")
print(a_star2(graph, 0, 9))