"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from search import dfs, bfs, a_star, dijkstra, branch_and_bound


if __name__ == "__main__":
    grafo = read_graph("mapas\mini_map.txt")

    caminho = bfs(grafo, 0, 7)
    print(caminho)