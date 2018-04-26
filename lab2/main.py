from dijkstra import Dijkstra, Dijkstra_heap
from graphs import gen_graph, invert_graph_to_edges

q = 1
r = 10 ** 6

with open('time_d4.txt', 'a') as file1:
    with open('time_m.txt', 'a') as file2:
        for n in range(100, 10001, 100):
            m = int(n ** 2 / 10)

            G = gen_graph(n, m, q, r)

            time_m = Dijkstra(G, 0)
            time_h = Dijkstra_heap(invert_graph_to_edges(G), 0, 4)

            file1.write(str(time_h) + ' ')
            file2.write(str(time_m) + ' ')
            file1.flush()
            file2.flush()

            print("n : {}\t m : {}\t heap time: {}\t mark time: {}".format(n, m, time_h, time_m))
            #print("n : {}\t m : {}\t mark time: {}".format(n, m, time_m))