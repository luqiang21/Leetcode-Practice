from helper_functions import find_next_node, frontier_path, eucledian_distance


import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
def shortest_path1(G, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    position = G.intersections
    G = G.roads
    frontier_set = {}
    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            return frontier_path(frontier_set, current, start)
        neighbors = G[current]
        for next in neighbors:
            new_cost = cost_so_far[current] + eucledian_distance(current, next, position)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + eucledian_distance(goal, next, position)
                frontier.put(next, priority)
                came_from[next] = current
                frontier_set[next] = current

    return came_from, cost_so_far

"""Method 2"""
def shortest_path(G, start, goal):
    """
    A* search Implementation.

    Returns the lowest cost path from start to goal.
    """

    # Get the interections, roads and the number of nodes
    position = G.intersections
    G = G.roads
    total_nodes = len(G)

    # initialize empty sets for the nodes in explored and frontier sets
    # Taking advantage of sets over list here
    explored = set()
    frontier = set([start])
    frontier_set = {}

    # A* search heuristicZ: f = g + heuristic
    # for all the nodes set the f_cost and g_cost at a high value during initialization

    g_cost = [999999 for _ in range(total_nodes)]
    f_cost = [999999 for _ in range(total_nodes)]

    # As per the equation, at the start node the path cost is 0.
    # Set g_cost at starting node to be 0.0 and the f_cost takes the value determined by heuristic.

    g_cost[start] = 0.0
    f_cost[start] = eucledian_distance(start, goal, position)

    # The main algorithm that loops across various nodes and then determines
    # the nodes in frontiers and finds the next node based on lowest f. Process continues
    # till we reach the goal.
    while frontier:
        current = find_next_node(frontier, f_cost)
        if current == goal:
            return frontier_path(frontier_set, current, start)  # if we reach/start from the goal return it

        frontier.remove(current)    # if we don't reach the goal, move the current node from frontier to explored
        explored.add(current)
        neighbors = G[current]

        for neighbor in neighbors:
            current_g_cost = g_cost[current] + eucledian_distance(current, neighbor, position)
            if neighbor not in explored or current_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = current_g_cost
                f_cost[neighbor] = current_g_cost + eucledian_distance(goal, neighbor, position)
                frontier_set[neighbor] = current
                frontier.add(neighbor)
                explored.add(neighbor)

    return None
