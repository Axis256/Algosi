from collections import defaultdict
import random


def gen_graph(n: int, m: int, q: int, r: int):
    if n < 2:
        raise ValueError
    if m > (n * (n - 1) / 2):
        raise ValueError
    if m < n - 1:
        raise ValueError
    generator = random.SystemRandom()
    graph = [[0 for x in range(0, n)] for y in range(0, n)]
    for i in range(0, n - 1):
        graph[i][i + 1] = graph[i + 1][i] = generator.randint(q, r)
    for i in range(0, m - n + 1):
        a = b = 0
        while True:
            a = generator.randint(0, n - 1)
            b = generator.randint(0, n - 1)
            if (a > b + 1 or a < b - 1) and graph[a][b] == 0:
                break
        graph[a][b] = graph[b][a] = generator.randint(q, r)
    return graph


def invert_graph_to_edges(graph):
    edges = defaultdict(dict)
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                edges[i][j] = graph[i][j]
    return edges
