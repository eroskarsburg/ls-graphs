"""Implementação da busca em profundidade."""
from heapq import heapify, heappush, heappop
import sys

class Stack:
    def __init__(self):
        self.items = []
        self.visited_items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("A pilha está vazia.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("A pilha está vazia.")
            return None

    def visited(self, value):
        return value in self.visited_items

    def size(self):
        return len(self.items)

def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    
    stack = [ (start,None) ]
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
            for key, value in graph[v[0]][1]:
                stack.append( (key, v[0], value) )


def dfs2(graph, start: int, goal: int) -> (int, float, [int]):
    s = Stack()
    s.push(start)
    best_cost = sys.maxsize
    node = 0
    while not s.is_empty():
        node = s.pop()
        if goal == node:
            break
        if not s.visited(node):
            s.visited_items.append(node)
            for neighbor in graph[node][1]:
                cost = neighbor[1]
                if cost < best_cost:
                    best_cost = cost
                    cur_node = neighbor[0]
                    s.push(cur_node)
    return node
                
            # processa_caminho(v)
            # set_visited(v)
            # for u in Grafo.neighbors(v):
            #     S.push(u)


def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    with open(filename, "rt") as input_file:
        vertex_count = int(input_file.readline().strip())
        graph = [[] for _ in range(vertex_count)]

        for _ in range(vertex_count):
            index, latitude, longitude = input_file.readline().strip().split()
            graph[_].append((latitude, longitude))
            graph[_].append([])

        for _ in range(int(input_file.readline().strip())):
            from_vertex, to_vertex, cost = input_file.readline().strip().split()
            graph[int(from_vertex)][1].append([int(to_vertex), float(cost)])
            graph[int(to_vertex)][1].append([int(from_vertex), float(cost)])
    return graph


grafo = read_graph("lib\mapas\mini_map.txt")
print(dfs(grafo, 0, 7))