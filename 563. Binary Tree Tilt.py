"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of
all left subtree node values and the sum of all right subtree node values. Null
node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""

from tools import timing

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    @timing
    def findTilt1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (not root.left and not root.right):
            return 0

        res = abs(self.sum(root.left) - self.sum(root.right))

        return res + self.findTilt1(root.left) + self.findTilt1(root.right)

    def sum(self, root):
        if not root:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)

    @timing
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[1]
    # avoid unnecessary computation
    def helper(self, root):

        # return (sum, tilt)
        if not root:
            return (0, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        return left[0] + right[0] + root.val, abs(left[0] - right[0]) + left[1] + right[1]

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
assert Solution().findTilt1(n1) == 1
assert Solution().findTilt(n1) == 1
