import sys
#region [ other graphs implementations to use later]
# class Graph:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    
#     def adiciona_aresta(self, u, v, peso):
#         self.grafo[u-1][v-1] = peso
#         self.grafo[v-1][u-1] = peso

 
#     def mostra_matriz(self):
#         #matriz de adjacencias
#         for i in range(self.vertices):
#             print(self.grafo[i])

# def read_graph(filename: str):
#     """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
#     graph = []
#     with open(filename, "rt") as input_file:
#         vertex_count = int(input_file.readline().strip())
#         for _ in range(vertex_count):
#             index, latitude, longitude = input_file.readline().strip().split()
#             index, latitude, longitude = [ int(index), float(latitude), float(longitude) ]
#             graph.append([(latitude, longitude),{}])
            
#         edge_count = int(input_file.readline().strip())
#         for _ in range(edge_count):
#             from_vertex, to_vertex, cost = (
#                 input_file.readline().strip().split()
#             )
#             from_vertex, to_vertex, cost = [ int(from_vertex), int(to_vertex), float(cost) ]
#             graph[from_vertex][1][to_vertex] = cost
    
#     return graph
#endregion
class Graph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.adjacency_list = [[] for _ in range(num_nodes)]
        self.coordinates = {}

    def add_node(self, node: int, latitude: float, longitude: float):
        self.coordinates[node] = (latitude, longitude)

    def add_edge(self, node1: int, node2: int, cost: float):
        self.adjacency_list[node1].append((node2, cost))
        self.adjacency_list[node2].append((node1, cost))


# Função para ler o grafo a partir de um arquivo
def read_graph(filename: str) -> Graph:
    with open(filename, 'r') as file:
        num_nodes = int(file.readline())
        graph = Graph(num_nodes)
        for _ in range(num_nodes):
            node, latitude, longitude = map(float, file.readline().split())
            graph.add_node(int(node), latitude, longitude)
        num_edges = int(file.readline())
        for _ in range(num_edges):
            node1, node2, cost = map(int, file.readline().split())
            graph.add_edge(node1, node2, cost)
    return graph