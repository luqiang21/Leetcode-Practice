from queue import Queue
import pprint


class BFSInfo():
    def __init__(self, srcDistance = None, predecessor = None):
        self.srcDistance = srcDistance
        self.predecessor = predecessor


def doBFS(graph, source):
    bfsInfo = []
    for i in range(len(graph)):
        bfsInfo.append(BFSInfo())

    bfsInfo[source].srcDistance = 0

    q = Queue()
    q.put(source)

    # Traverse the graph

    # As long as the queue is not empty:
    #  Repeatedly dequeue a vertex u from the queue.
    #
    #  For each neighbor v of u that has not been visited:
    #     Set distance to 1 greater than u's distance
    #     Set predecessor to u
    #     Enqueue v
    #
    #  Hint:
    #  use graph to get the neighbors,
    #  use bfsInfo for distances and predecessors
    visited = set([source])
    while not q.empty():

        u = q.get()
        # print(u, graph[u])
        # print(q.queue)
        for v in graph[u]:

            if v not in visited:
                q.put(v)
                visited.add(v)
                bfsInfo[v].predecessor = u
                bfsInfo[v].srcDistance = bfsInfo[u].srcDistance + 1

    return bfsInfo


graph = [[1], [0, 4, 5], [3, 4, 5], [2, 6], [1, 2], [1, 2, 6], [3, 5], []]
print('graph:\nnode: adjacent nodes')
pprint.pprint([[i, neighbors] for i, neighbors in enumerate(graph)])
print('\nafter bfs\nnode: (srcDistance, predecessor)')
pprint.pprint([[i, (node.srcDistance, node.predecessor)] for i, node in
               enumerate(doBFS(graph, 3))])
# TODO complete backtracking to show the visited sequence

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}
def BFS(graph, start):
    '''
    breadth first search
    Args:
        graph: dictionay stores adjacent nodes
        start: the node to start BFS traversal
    Returns:
        BFS sequence of nodes
    '''
    from queue import deque
    queue = deque()
    queue.append(start)
    explored = []

    while queue:
        node = queue.popleft()
        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
            explored.append(node)
    return explored
    
print(BFS(graph, 'A'))

def BFS_shortest_path(graph, start, goal):
    '''
    breadth first search
    Args:
        graph: dictionay stores adjacent nodes
        start: the node to start
        goal: the goal node
    Returns:
        the shortest path
    '''
    from queue import deque
    queue = deque() # stores path instead of node
    queue.append([start])
    explored = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = path[:]
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path
            explored.append(node)
    return "sorry, no path found"

print(BFS_shortest_path(graph, 'G', 'D') )
