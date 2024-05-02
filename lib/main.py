"""Utilize este arquivo para depurar seus algoritmos."""

from graph import Graph, read_graph
from search import dfs, bfs, a_star, branch_and_bound, dijkstra


if __name__ == "__main__":
    g = Graph()
    g.grafo = read_graph("lib\mapas\mini_map.txt")
    #print("DFS: " + dfs(g.grafo, 0, 9))
    #print("BFS: " + bfs(g.grafo, 0, 9))
    #print("BRANCH AND BOUND: " + branch_and_bound(g.grafo, 0, 7))
    print(a_star(g.grafo, 0, 9))
    #print("DIJKSTRA: " + dijkstra(g.grafo, 0, 9))