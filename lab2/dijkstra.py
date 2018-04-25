import timeit
from heap import Heap


def Dijkstra(edges, start, d):
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
    return (end - begin)