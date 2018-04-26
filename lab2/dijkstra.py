import timeit
from collections import defaultdict
from heapq import *
from heap import Heap


def Dijkstra_heap_fast(edges, f, t):
    begin = timeit.default_timer()

    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen = [(0, f, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                end = timeit.default_timer()
                return end - begin

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    end = timeit.default_timer()

    return end - begin


def Dijkstra_heap(edges, start, d):
    begin = timeit.default_timer()

    A = [None] * len(edges)
    queue = Heap(d)
    queue.insert((0, start))
    while queue.size != 0:
        path_len, v = queue.pop()
        if A[v] is None:  # v is unvisited
            A[v] = path_len
            for w, edge_len in edges[v].items():
                if A[w] is None:
                    queue.insert((path_len + edge_len, w))

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