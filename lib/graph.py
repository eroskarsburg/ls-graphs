import sys
class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    
    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

 
    def mostra_matriz(self):
        #matriz de adjacencias
        for i in range(self.vertices):
            print(self.grafo[i])


def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    graph = []
    with open(filename, "rt") as input_file:
        vertex_count = int(input_file.readline().strip())
        for _ in range(vertex_count):
            index, latitude, longitude = input_file.readline().strip().split()
            index, latitude, longitude = [ int(index), float(latitude), float(longitude) ]
            graph.append([(latitude, longitude),{}])
            
        edge_count = int(input_file.readline().strip())
        for _ in range(edge_count):
            from_vertex, to_vertex, cost = (
                input_file.readline().strip().split()
            )
            from_vertex, to_vertex, cost = [ int(from_vertex), int(to_vertex), float(cost) ]
            graph[from_vertex][1][to_vertex] = cost
    
    return graph
