import heapq
import math
import util

class PriorityQueue:
    def __init__(self, start = 0, goal = 0):
        self._start_node = start
        self._goal_node = goal
        self.priority = 0
        self.cur_node = 0
        self.came_from = {}
        self.cost_so_far = 0
        self.came_from[start] = None
        self.new_graph = []
        
    def set(self):
        self.heap = [(0, self._start_node)]
    
    def set_priority(self, neighbor):
        lat1, lon1 = self.new_graph[self._goal_node]["coords"]["x"], self.new_graph[self._goal_node]["coords"]["y"]
        lat2, lon2 = self.new_graph[neighbor]["coords"]["x"], self.new_graph[neighbor]["coords"]["y"]
        self.priority = self.cost_so_far + haversine(lat1, lon1, lat2, lon2)
    
    def push(self, priority, neighbor):
        heapq.heappush(self.heap, (priority, neighbor))

    def pop(self):
        return heapq.heappop(self.heap)[1]
    
    def isEmpty(self):
        if (self.heap == []):
            return True
        else:
            return False


class ValorGraph:
    def __init__(self) -> None:
        self.position = Position()


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


def doDictGraph(graph):
    dict = {}
    for ponto in range(len(graph)):
        dictVisinhos = {}
        for visinho in graph[ponto][1]:
            dictVisinhos[visinho[0]] = visinho[1]
        x = float(graph[ponto][0][0])
        y = float(graph[ponto][0][1])
        dict[ponto] = {
            "coords": {"x": x, "y": y},
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
            "coords": {"x": x, "y": y},
            "neighbors": dictVisinhos,
            "cost": float("inf"),
            "closed_list": [],
            "goalDistance": 0,
        }
    return dict


def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    f = PriorityQueue(start=start, goal=goal)
    f.new_graph = makeDict2(graph, goal)
    f.set()
    path = list()
    closed_list = set()
    cost = f.new_graph[start]["cost"] = 0
    prodec_cost = 0
    heurist = 0
    while not f.isEmpty():
        f.cur_node = f.pop()
        if f.cur_node == goal:
            closed_list.add(f.cur_node)
            break
        if f.cur_node in closed_list:
            closed_list.add(f.cur_node)
            continue
        if len(f.new_graph[f.cur_node]["neighbors"]) == 0:
            continue
        closed_list.add(f.cur_node)
        for neighbor in f.new_graph[f.cur_node]["neighbors"]:
            #heuristic
            #f = g + h
            f.cost_so_far = (f.new_graph[f.cur_node]["cost"] + f.new_graph[f.cur_node]["neighbors"][neighbor])
            if f.cost_so_far < f.new_graph[neighbor]["cost"]:
                if neighbor not in closed_list:
                    f.new_graph[neighbor]["cost"] = f.cost_so_far
                    f.set_priority(neighbor)
                    f.push(f.priority, neighbor)
                    f.new_graph[neighbor]["closed_list"] = f.cur_node
                else:
                    continue
    nodes_distance = util.heuristic(f.new_graph[start], f.new_graph[goal])
    f.cur_node = goal
    while f.cur_node != start:
        path.append(f.cur_node)
        f.cur_node = f.new_graph[f.cur_node]["closed_list"]
    path.append(start)
    path.reverse()
    return len(closed_list), f.new_graph[goal]["cost"], path
