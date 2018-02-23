'''
The car manufacturer Honda holds their distribution system in the form of a tree
(not necessarily binary). The root is the company itself, and every node in the
tree represents a car distributor that receives cars from the parent node and
ships them to its children nodes. The leaf nodes are car dealerships that sell
cars direct to consumers. In addition, every node holds an integer that is the
cost of shipping a car to it.

Take for example the tree below:

alt

A path from Honda’s factory to a car dealership, which is a path from the root
to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the
sum of the costs for every node in the path. For example, in the tree above one
Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given
a node rootNode, write an function getCheapestCost that calculates the minimal
Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and
space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in
the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

Constraints:

[time limit] 5000ms

[input] Node rootNode

0 ≤ rootNode.cost ≤ 100000
[output] integer

'''


def get_cheapest_cost(rootNode):
  children = rootNode.children
  if children == []:
    return rootNode.cost
  print(rootNode.cost)
  min_cost = 100000
  for child in children:
    current_cost = get_cheapest_cost(child)
    if min_cost > current_cost:
      min_cost = current_cost

  return min_cost + rootNode.cost

def get_n_of_longest_path(rootNode):
  children = rootNode.children
  if children == []:
    return 1#rootNode.cost
  max_path = 0
  for child in children:
    current_path = get_n_of_longest_path(child)
    if max_path < current_path:
      max_path = current_path

  return max_path + 1

def get_longest_path(rootNode):
  children = rootNode.children
  if children == []:
    return [rootNode.cost], 1#rootNode.cost
  max_length = 0
  for child in children:
    current_path, length = get_longest_path(child)
    if max_length < length:
      next_ = current_path
      max_length = length

  return [rootNode.cost] + next_, max_length + 1

##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

''' graph:
        0
1       2       3
4      5 6     7 8
       9 10
       11
'''
n1 = Node(0)
n2 = Node(5)
n3 = Node(3)
n4 = Node(6)
n5 = Node(4)
n6 = Node(2)
n7 = Node(0)
n8 = Node(1)
n9 = Node(5)
n10 = Node(1)
n11 = Node(10)
n12 = Node(1)
n1.children = [n2, n3, n4]
n2.children = [n5]
n3.children = [n6, n7]
n4.children = [n8, n9]
n6.children = [n10]
n7.children = [n11]
n10.children = [n12]

print('the cheapest path is', get_cheapest_cost(n1))
print('the length of longest path is', get_n_of_longest_path(n1))
print('the longest path is', get_longest_path(n1)[0])
