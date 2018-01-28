from math import sqrt
import heapq

def find_next_node(frontier, f_cost):
    """
    This is used to find the least value of f, which plays ball in finding
    the index of next node.
    """
    next_node_index = None   # initialize current index
    f_cost_min = 999999  # initialize lowest_f with a high value
    for index in frontier:
        f = f_cost[index]
        # check and pick the index with lowest f_cost
        if f < f_cost_min:
            next_node_index = index
            f_cost_min = f
    return next_node_index

def frontier_path(frontier_set, current, start):
    """
    This function reconstructs the path so far.
    """
    path = []
    while current != start:
        path.insert(0, current)
        current = frontier_set[current]
    path.insert(0, start)  # insert at the start
    return path
    
    
def eucledian_distance(start, goal, position):
    """
    Function to find the shortest distance between 2 given points.
    """
    x1, y1 = position[start]
    x2, y2 = position[goal]
    dist = sqrt( (x2-x1)**2 + (y2-y1)**2 )
    return dist