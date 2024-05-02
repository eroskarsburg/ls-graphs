import math

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

#
# Não altere este comentário e adicione suas funções ao final do arquivo.
#

