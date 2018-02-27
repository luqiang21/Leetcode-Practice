'''
https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
Consider an undirected graph consisting of n nodes where each node is labeled from
1 to n and the edge between any two nodes is always of length 6. We define node s to
be the starting position for a BFS.

Given q queries in the form of a graph and some starting node, s , perform each query
by calculating the shortest distance from starting node s to all the other nodes
in the graph. Then print a single line of n-1 space-separated integers listing node's
shortest distance to each of the n-1 other nodes (ordered sequentially by node number);
if s is disconnected from a node, print -1 as the distance to that node.

'''

from tools import timing
class Graph():
    def __init__(self, n):
        self.n = n
        self.adjacent = {i:[] for i in range(n)}

    def connect(self, x, y):
        self.adjacent[x].append(y)
        self.adjacent[y].append(x)

    def find_all_distances(self, s):
        dis = [-1 for i in range(self.n)]
        start = s

        visited = []
        explored = []
        from queue import deque
        q = deque()
        q.append(start)
        dis[s] = 0

        while q:
            node = q.popleft()
            if node not in explored:
                neighbors = self.adjacent[node]
                distance = dis[node]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        q.append(neighbor)
                        dis[neighbor] = distance + 6
                explored.append(node)
        dis.pop(s)
        print(" ".join(map(str,dis)))


n, m = 4, 2
edges = [[1, 2], [1, 3]]
graph = Graph(n)
for i in range(m):
    x, y = edges[i]
    graph.connect(x-1,y-1)
s = 1
graph.find_all_distances(s-1)

n, m = 3, 1
edges = [[2, 3]]
graph1 = Graph(n)
for i in range(m):
    x, y = edges[i]
    graph1.connect(x-1,y-1)
s = 2
graph1.find_all_distances(s-1)
