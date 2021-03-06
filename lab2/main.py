from dijkstra import Dijkstra, Dijkstra_heap
from graphs import *

q = 1
r = 10 ** 6

with open('time_hq - b.txt', 'a') as file1:
    with open('time_m - b.txt', 'a') as file2:
        for n in range(100, 10001, 100):
            m = int(n * (n - 1) / 2)

            G = gen_comp_graph(n, m, q, r)

            time_m = Dijkstra(G, 0)
            time_h = Dijkstra_heap(invert_graph_to_edges(G), 0)

            file1.write(str(time_h) + ' ')
            file2.write(str(time_m) + ' ')
            file1.flush()
            file2.flush()

            print("n : {}\t m : {}\t heap time: {}\t mark time: {}".format(n, m, time_h, time_m))
            #print("n : {}\t m : {}\t mark time: {}".format(n, m, time_m))