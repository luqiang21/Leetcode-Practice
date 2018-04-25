"""

The thief has found himself a new place for his thievery again. There is only
one entrance to this area, called the "root." Besides the root, each house has
one and only one parent house. After a tour, the smart thief realized that "all
houses in this place forms a binary tree". It will automatically contact the
police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting
the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
from tools import timing
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
mem = {}

class Solution:
    @timing
    def rob1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # compute val which is root.val + next not directly linked nodes
        val = root.val
        if root.left:
            val += self.rob1(root.left.left) + self.rob1(root.left.right)

        if root.right:
            val += self.rob1(root.right.left) + self.rob1(root.right.right)

        return max(val, self.rob1(root.left) + self.rob1(root.right))

    @timing
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if root in mem:
            return mem[root]

        # compute val which is root.val + next not directly linked nodes
        val = root.val
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)

        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)

        mem[root] = max(val, self.rob(root.left) + self.rob(root.right))
        return max(val, self.rob(root.left) + self.rob(root.right))

    @timing
    def rob2(self, root):
        if not root:
            return 0
        return max(self.rob_helper(root))

    def rob_helper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return two elements, (not include root.val, include root.val)
        if not root:
            return (0, 0)

        left = self.rob_helper(root.left)
        right = self.rob_helper(root.right)

        return max(left) + max(right), root.val + left[0] + right[0]

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

assert Solution().rob1(root) == 9
assert Solution().rob(root) == 9
assert Solution().rob2(root) == 9
