from collections import deque


def FloydWarshall(graph):
    n = len(graph)
    dists = [[graph[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and i != k and j != k and dists[i][k] + dists[k][j] < dists[i][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
    return dists


def spfa(graph, node):
    n, que = len(graph), deque()
    que.append((0, node))
    dists = [float("inf") for _ in range(n)]
    dists[node] = 0

    while que:
        (dist, vertex) = que.popleft()

        for i in range(n):
            val = graph[vertex][i]
            if val != float("inf") and dist + val < dists[i]:
                dists[i] = dist + val
                que.append((dists[i], i))
    return dists


if __name__ == '__main__':
    n = int(input())
    graphData = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        p, q, d = map(int, input().split())
        graphData[p - 1][q - 1] = d
        graphData[q - 1][p - 1] = d
    # print(graphData)

    # ans = 0

    # distances = FloydWarshall(graphData)
    # # print(distances)
    # for d in distances:
    #     ans = max(ans, max([i for i in d if i != float("inf")]))
    # # print(ans)

    # for i in range(n):
    #     distances = spfa(graphData, i)
    #     # print(distances)
    #     ans = max(ans, max([j for j in distances if j != float("inf")]))

    dists1 = spfa(graphData, 0)
    # print(dists1)
    far = max([j for j in dists1 if j != float("inf")])
    # print(f"far = {far}, dists1.index(far) = {dists1.index(far)}")
    dists2 = spfa(graphData, dists1.index(far))
    # print(dists2)
    ans = max([j for j in dists2 if j != float("inf")])

    print(ans * 10 + sum([i for i in range(ans + 1)]))
