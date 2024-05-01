import heapq
import math
import sys
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

        
def makehuristikdict():
    h = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

def heuristic(node, values):
    return values[node]

def astar(graph, start, end):
    dic = dict_maker(graph)
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()
    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []
    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)
        if (current == end):
            break
        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)
            #print(new.city, new.distance, "now : " + str(distance[current]), g_cost)
            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                #print(f_cost)
                q.push(new.city, f_cost)
                path[new.city] = current
    printoutput(start, end, path, distance, expandedList)

def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end
    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("A-star Agorithm for Romania Map")
    print("\tArad => Bucharest")
    print("=======================================================")
    print("List of Cities that are Expanded : " + str(expandedlist))
    print("Total Number of Cities that are Expanded : " + str(len(expandedlist)))
    print("=======================================================")
    print("Cities in Final path : " + str(finalpath))
    print("Total Number of cities in final path are : " + str(len(finalpath)))
    print("Total Cost : " + str(distance[end]))


def a_star(graph, start, goal):
    dict = dict_maker(graph)
    start_node = dict[start]
    goal_node = dict[goal]
    closed_list = set()
    opened_list = set()
    cur_node = -1
    g = 0 # custo do node atual até o node final
    h = 0 # custo do node atual até o node inicial
    best_cost = 10000000

    while range(len(dict)):
        cur_node = cur_node+1
        if cur_node in closed_list:
            continue
        closed_list.add(cur_node)
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


## MAIN CODE
graph = read_graph("lib\mapas\mini_map.txt")

start = "Arad"
goal = "Bucharest"
start = 0
goal = 9
a_star(graph, start, goal)


print(a_star(graph, 0, 9))
visited_nodes, optimal_nodes = AStarSearch()
print('visited nodes: ' + str(visited_nodes))
print('optimal nodes sequence: ' + str(optimal_nodes))
