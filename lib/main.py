"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from search import dfs, bfs, a_star, dijkstra, branch_and_bound


if __name__ == "__main__":
    grafo = read_graph("mapas\mini_map.txt")

    print(bfs(grafo, 0, 7))
    #print(dfs(grafo, 0, 7))
    #print(branch_and_bound(grafo, 0, 7))
    #print(a_star(grafo, 0, 7))
    #print(dijkstra(grafo, 0, 7))