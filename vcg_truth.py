#!/usr/bin/env python3
import networkx as nx
import doctest
import numpy as np


def vcg_cheapest_path(graph, source, target):
    """
    # From class
    >>> G = nx.Graph()
    >>> edges = [('A', 'B', 3), ('A', 'C', 5), ('A', 'D', 10), ('B', 'C', 1), ('B', 'D', 4), ('C', 'D', 1)]
    >>> G.add_weighted_edges_from(edges)
    >>> vcg_cheapest_path(G, 'A', 'D')
    Cost from A to B : -4
    Cost from B to C : -2
    Cost from C to D : -3
    >>> G = nx.Graph()
    >>> edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 5), ('B', 'D', 4), ('C', 'D', 3), ('C', 'E', 10), ('D', 'E', 21), ('D', 'F', 2), ('E', 'F', 5)]
    >>> G.add_weighted_edges_from(edges)
    >>> vcg_cheapest_path(G, 'A', 'F')
    Cost from A to B : -3
    Cost from B to D : -6
    Cost from D to F : -14
    >>> G = nx.Graph()
    >>> edges = [('A', 'B', 10), ('A', 'C', 8), ('B', 'C', 6), ('A','D',5), ('B','D',2),('C','D',1)]
    >>> G.add_weighted_edges_from(edges)
    >>> vcg_cheapest_path(G, 'A', 'C')
    Cost from A to D : -7
    Cost from D to C : -3
    >>> G = nx.Graph()
    >>> edges = [('A', 'B', 1), ('A', 'C', 1), ('A', 'D', 1), ('A','E',1), ('B','C',1),('B','D',1),('B','E',1),('C','D',1),('C','E',1),('D','E',1)]
    >>> G.add_weighted_edges_from(edges)
    >>> vcg_cheapest_path(G, 'A', 'E')
    Cost from A to E : -2
    """
    path = nx.shortest_path(graph, source, target, weight="weight")

    edges = list()

    for i in range(len(path)):
        if i != len(path) - 1:
            edges.append((path[i], path[i + 1]))

    for u, v in edges:
        g_other = nx.Graph(graph)
        g_other.remove_edge(u, v)
        distance = -nx.shortest_path_length(g_other, source, target, "weight")
        for i, j in edges:
            if (u, v) != (i, j):
                distance += g_other.get_edge_data(i, j)["weight"]
        print(f"Cost from {u} to {v} : {distance}")


if __name__ == "__main__":
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
