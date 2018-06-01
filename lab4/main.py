from random import randint

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def BFS(self, s, t, parent):

        visited = [False]*(self.row)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] is False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False


    def minimum_cut(self, source, sink):

        parent = [-1]*(self.row)
        min_cut = 0

        while self.BFS(source, sink, parent):
            min_path = float("Inf")
            s = sink
            while(s != source):
                min_path = min(min_path, self.graph[parent[s]][s])
                s = parent[s]

            min_cut += min_path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= min_path
                self.graph[v][u] += min_path
                v = parent[v]

        return min_cut

e1 = randint(1, 10)
e2 = randint(1, 10)
e3 = randint(1, 10)
e4 = randint(1, 10)

graph = [[0, randint(1, 10), randint(1, 10), 0, 0, 0 ],
         [0, 0, 0, e1, e2, 0],
         [0, 0, 0, e3, e4, 0],
         [0, e1, e3, 0, 0, randint(1, 10)],
         [0, e2, e4, 0, 0, randint(1, 10)],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

for line in graph:
    print(line)

print("Maximum flow: %d " % g.minimum_cut(source, sink))

#for line in graph:
#    print(line)
