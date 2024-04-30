"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from search import dfs as d, bfs as b, a_star as aS, dijkstra as dij, branch_and_bound as bab


if __name__ == "__main__":
    grafo = read_graph("mapas\mini_map.txt")

    print(b.bfs(grafo, 0, 7))
    #print(d.dfs(grafo, 0, 7))
    #print(bab.branch_and_bound(grafo, 0, 7))
    #print(aS.a_star(grafo, 0, 7))
    #print(dij.dijkstra(grafo, 0, 7))