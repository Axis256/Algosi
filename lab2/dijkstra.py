import timeit
from heapq import *


def Dijkstra_heap(edges, start):
    begin = timeit.default_timer()

    A = [None] * len(edges)
    queue = []
    heappush(queue, (0, start))
    while len(queue) != 0:
        path_len, v = heappop(queue)
        if A[v] is None:  # v is unvisited
            A[v] = path_len
            for w, edge_len in edges[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    # to give same result as original, assign zero distance to unreachable vertices
    # return [0 if x is None else x for x in A]
    end = timeit.default_timer()
    return end - begin

def Dijkstra(graph, start):
    begin = timeit.default_timer()

    size = len(graph)
    valid = [True] * size
    weight = [1000000] * size
    weight[start] = 0
    for i in range(size):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(size):
            if weight[ID_min_weight] + graph[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + graph[ID_min_weight][i]
        valid[ID_min_weight] = False
    end = timeit.default_timer()
    return end - begin