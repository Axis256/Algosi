from dijkstra import Dijkstra
from graphs import gen_graph, invert_graph_to_edges

q = 1
r = 10 ** 6

with open('time_d4.txt', 'w') as file:
    for n in range(100, 10001, 100):
        m = int(n ** 2 / 10)

        G = gen_graph(n, m, q, r)

        time = Dijkstra(invert_graph_to_edges(G), 0, 2)

        file.write(str(time) + ' ')

        print("n : {}\t m : {}\t time: {}".format(n, m, time))