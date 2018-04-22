"""

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
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
    def isBalanced1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # edge case
        if root is None:
            return True
        # comparison
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        # make sure subtree is balanced
        if self.isBalanced1(root.left) and self.isBalanced1(root.right):
            return True

        return False

    def height(self, root):
        if root is None:
            return 0
        l_height = self.height(root.left)
        r_height = self.height(root.right)

        return max(l_height, r_height) + 1

    def depth_balance(self, root):
        # edge case
        if root is None:
            return 0, True

        left_depth, left_bal = self.depth_balance(root.left)
        right_depth, right_bal = self.depth_balance(root.right)

        cur_bal = abs(left_depth - right_depth) <= 1

        return max(left_depth, right_depth) + 1, left_bal and right_bal and cur_bal

    @timing
    def isBalanced2(self, root):
        return self.depth_balance(root)[1]

    def dfsHeight(self, root):
        if root is None:
            return 0
        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1
    @timing
    def isBalanced(self, root):
        return self.dfsHeight(root) != -1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

assert Solution().isBalanced1(root) == True
assert Solution().isBalanced2(root) == True
assert Solution().isBalanced(root) == True
