"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]

"""

#
# Definition for binary tree:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    
def largestValuesInTreeRows(t):
    res = []
    from queue import deque

    if not t:
        return []
    q = deque([t])
    explored = []

    while q:
        res.append(max(n.value for n in q))
        new_q = deque()

        for node in q:
            if node.left:
                new_q.append(node.left)
            if node.right:
                new_q.append(node.right)
        q = new_q
    return res
