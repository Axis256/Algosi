import sys
from graphs import *
import timeit


def MSP_KRUSKAL(n, edges):      # edges = [(weight, start, end), ...]
    begin = timeit.default_timer()

    MSP = []
    edges.sort()
    comp = [i for i in range(n)]
    for weight, start, end in edges:
        if comp[start] != comp[end]:
            MSP.append((start, end))
            a = comp[start]
            b = comp[end]
            for i in range(n):
                if comp[i] == b:
                    comp[i] = a

    end = timeit.default_timer()
    MSP.clear()
    return (end - begin)


def MSP_PRIM(n, graph):
    begin = timeit.default_timer()

    MSP = []
    used = [False for i in range(n)]         # visited vertices
    min_e = [sys.maxsize for i in range(n)]  # min distance from curr verticle to others
    sel_e = [-1 for i in range(n)]           # second part of the edge
    min_e[0] = 0

    for i in range(n):
        v = -1
        for j in range(n):
            if (not used[j] and (v == -1 or min_e[j] < min_e[v])):
                v = j

        if (min_e[v] == sys.maxsize):
            print("No MST")
            sys.exit()

        used[v] = True
        if (sel_e[v] != -1):
            MSP.append((v, sel_e[v]))

        for to in range(n):
            if (graph[v][to] < min_e[to] and graph[v][to] != 0):
                min_e[to] = graph[v][to]
                sel_e[to] = v

        end = timeit.default_timer()
        MSP.clear()
        return (end - begin)

q = 1
r = 10 ** 6

with open('time_prim b.txt', 'a') as file1:
    with open('time_kruskal b.txt', 'a') as file2:
        for n in range(100, 10001, 100):
            m = int(n * (n - 1) // 2)

            G = gen_comp_graph(n, m, q, r)

            time_prim = MSP_PRIM(n, G)
            time_kruskal = MSP_KRUSKAL(n, invert_graph_to_edges(n, G))

            file1.write(str(time_prim) + ' ')
            file2.write(str(time_kruskal) + ' ')
            file1.flush()
            file2.flush()

            print("n : {}\t m : {}\t time_prim : {}\t time_kruskal : {}".format(n, m, time_prim, time_kruskal))
            #print("n : {}\t m : {}\t time_prim : {}".format(n, m, time_prim))
