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


    def maximum_flow(self, source, sink):

        parent = [-1]*(self.row)
        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            print(path_flow)
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

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

print("The maximum possible flow is %d " % g.maximum_flow(source, sink))
