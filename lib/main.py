"""Utilize este arquivo para depurar seus algoritmos."""

from graph import Graph, read_graph
from search import dfs, bfs, a_star, branch_and_bound, dijkstra


if __name__ == "__main__":
    g = Graph()
    g.grafo = read_graph("lib\mapas\mini_map.txt")
    #print(a_star2(g.grafo, 0, 9))
    #print(b.bfs(grafo, 0, 7))
    #print(d.dfs(grafo, 0, 7))
    #print(bab.branch_and_bound(grafo, 0, 7))
    #print(aS.a_star(grafo, 0, 7))
    print(dijkstra(g.grafo, 0, 9))