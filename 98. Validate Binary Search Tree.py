"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

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
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # edge case
        if root is None:
            return True

        # initilization
        node_bounds_stack = [(root, -float('inf'), float('inf'))]

        # DFS
        while len(node_bounds_stack):
            node, lb, ub = node_bounds_stack.pop()

            if node.val <= lb or node.val >= ub:
                return False

            if node.left:
                node_bounds_stack.append((node.left, lb, node.val))
            if node.right:
                node_bounds_stack.append((node.right, node.val, ub))
        return True

    # recursive
    @timing
    def isValidBST(self, root, lb=-float('inf'), ub=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.val <= lb or root.val >= ub:
            return False

        return self.isValidBST(root.left, lb, root.val) and self.isValidBST(root.right, root.val, ub)

root = TreeNode(2)
l = TreeNode(1)
r = TreeNode(3)
root.left = l
root.right = r
assert Solution().isValidBST1(root) == True
assert Solution().isValidBST(root) == True


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

assert Solution().isValidBST1(root) == False
assert Solution().isValidBST(root) == False
