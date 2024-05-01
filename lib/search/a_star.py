import heapq
import math

class PriorityQueue:
    def __init__(self, start = 0, goal = 0):
        self._start_node = start
        self._goal_node = goal
        self.came_from = {}
        self.cost_so_far = {}
        self.came_from[start] = None
        self.cost_so_far[start] = 0
        self.new_graph = []
        
    def set(self):
        self.heap = [(0, self._start_node)]
    
    def push(self, priority, neighbor):
        heapq.heappush(self.heap, (priority, neighbor))

    def pop(self):
        return heapq.heappop(self.heap)[1]
    
    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False
        
    def check(self):
        print(self.cities)


class ValorGraph:
    def __init__(self) -> None:
        self.position = Position


class Position:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

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
    f = PriorityQueue(start=start, goal=goal)
    f.new_graph = makeDict2(graph, goal)
    f.new_graph[start]["custo"] = 0
    visitados = set()
    f.set()
    cur_node = 0

    while True:
        cur_node = f.pop()
        if cur_node in visitados:
            continue
        visitados.add(cur_node)
        if cur_node == goal:
            break
        for neighbor in f.new_graph[cur_node]["visinhos"]:

            best_cost = (
                f.new_graph[cur_node]["custo"]
                + f.new_graph[cur_node]["visinhos"][neighbor]
            )
            if best_cost < f.new_graph[neighbor]["custo"] and neighbor not in visitados:
                f.new_graph[neighbor][
                    "custo"
                ] = best_cost
                priority = best_cost + haversine(
                    f.new_graph[goal]["posicao"]["x"],
                    f.new_graph[goal]["posicao"]["y"],
                    f.new_graph[neighbor]["posicao"]["x"],
                    f.new_graph[neighbor]["posicao"]["y"],
                )
                f.push(priority, neighbor)
                f.new_graph[neighbor][
                    "anteriores"
                ] = cur_node
    path = []
    cur_node = goal
    while cur_node != start:
        path.append(cur_node)
        cur_node = f.new_graph[cur_node]["anteriores"]
    path.append(start)
    path.reverse()
    return len(visitados), f.new_graph[goal]["custo"], path


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