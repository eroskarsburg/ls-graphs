"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from search import dfs, bfs, a_star, branch_and_bound, dijkstra


if __name__ == "__main__":
    graph = read_graph("lib\mapas\mini_map.txt")
    print(dfs(graph, 0, 7))
    print(bfs(graph, 0, 7))
    print(branch_and_bound(graph, 0, 7))
    print(a_star(graph, 0, 7))
    print(dijkstra(graph, 0, 7))