import heapq

from functools import cmp_to_key
from collections import defaultdict
from Learn.DataStructure.UnionFindSet.template import UnionFindSet


def kruskal(graph: dict):
    tree, n = [], len(graph.get("nodes"))
    ufs = UnionFindSet(n + 1)
    graph.get("edges").sort(key=cmp_to_key(lambda a, b: a[2] - b[2]))
    for start, end, weight in graph.get("edges"):
        if len(tree) == n - 1:
            break
        if not ufs.same(start, end):
            ufs.union(start, end)
            tree.append((start, end, weight))
    return tree


def prim(graph: dict):
    tree, origin, visited, adjacent = [], graph["nodes"][0], set(), defaultdict(list)

    for start, end, weight in graph.get("edges"):
        adjacent[start].append((weight, start, end))
        adjacent[end].append((weight, end, start))

    visited.add(origin)
    adjacentEdges = adjacent[origin]
    heapq.heapify(adjacentEdges)
    while adjacentEdges:
        weight, start, end = heapq.heappop(adjacentEdges)
        if end not in visited:
            visited.add(end)
            tree.append((start, end, weight))

            for item in adjacent[end]:
                if item[2] not in visited:
                    heapq.heappush(adjacentEdges, item)
    return tree


if __name__ == '__main__':
    graphData = {
        "nodes": [1, 2, 3, 4, 5],
        "edges": [(1, 2, 1),
                  (1, 3, 3),
                  (1, 4, 5),
                  (2, 3, 2),
                  (2, 4, 4),
                  (2, 5, 6)]
    }

    res = kruskal(graphData)
    print(f"Kruskal = {res}")

    res = prim(graphData)
    print(f"Prim = {res}")
