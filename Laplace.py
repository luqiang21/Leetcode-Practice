# Convert a simple graph to a laplacian matrix

# Simple Graph: Undirected, (not a multigraph) At most 1 edge between 2 distinct nodes. No self-loop edges
# Laplacian Matrix: (D - A; D is degree matrix, A is adjacency matrix)
# L_{i, i} has degree of node i (number of incident edges on i)
# L_{i, j} has -1 if undirected edge exists between node i and j, and 0 otherwise.

# Define node structure and write converter function

# Example:
# [ 2, -1, -1, 0;
#  -1,  2, -1, 0;
#  -1, -1,  3, -1;
#   0,  0, -1, 1;]


# Input: one node object that can reach all other nodes in graph, over paths that may involve multiple edges
# Each node object is something that contains
# list of adjacent node objects (or pointers to other node objects)


# Output: Laplacian Matrix, in a 2d array
from random import random

class Node():
    def __init__(self, adj=None):
        self.adjList = adj # adj is a list of node objects ["node1", "node2"]
        self.id = random()    
from collections import deque
def converter(node):
    laplace_mat = []
    visited = set()
    q = deque()
    q.append(node)
    nodes = []
    connections = set()
    while q:
        top = q.popleft()
        visited.add(top.id)
        if top not in nodes:
            nodes.append(top)
        for n in top.adjList:
            connections.add((top, n))
            connections.add((n, top))
            if n.id not in visited:
                q.append(n)
    laplace_mat = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]   
    for i in range(len(nodes)):
        laplace_mat[i][i] = len(nodes[i].adjList)
    for con in connections:
        i, j = con
        laplace_mat[nodes.index(i)][nodes.index(j)] = -1

    return laplace_mat

ans = [[2, -1, -1, 0],
       [-1, 2, -1, 0],
       [-1, -1, 3, -1],
       [0, 0, -1, 1]]
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n1.adjList = [n2, n3]
n2.adjList = [n1, n3]
n3.adjList = [n1, n2, n4]
n4.adjList = [n3]

pprint = lambda matrix :  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]), '\n')
pprint(converter(n1))
pprint(converter(n3))
assert converter(n1) == ans
pprint(ans)
