"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

from tools import timing

@timing
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    @timing
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(preorder.pop(0))

        root_index = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index+1:])

        return root


    # iterative way
    @timing
    # iterative https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34555/The-iterative-solution-is-easier-than-you-think!
    def buildTree1(self, preorder, inorder):
        if not preorder:
            return None
        dic = {}
        stack = []
        for i, num in enumerate(inorder):
            dic[num] = i
        root = TreeNode(preorder[0])
        stack.append(root)

        for i in range(1,len(preorder)):
            node = TreeNode(preorder[i])

            if dic[node.val] < dic[stack[-1].val]:
                # the new node is on the left of the last node,
                # so it must be its left child (that's the way preorder works)
                stack[-1].left = node
            else:
                # the new node is on the right of the last node,
                # so it must be the right child of either the last node
                # or one of the last node's ancestors.
                # pop the stack until we either run out of ancestors
                # or the node at the top of the stack is to the right of the new node
                parent = None
                while len(stack) != 0 and dic[node.val] > dic[stack[-1].val]:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()
root = sol.buildTree(preorder, inorder)
print(root.val, root.left.val, root.right.val)
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = sol.buildTree1(preorder, inorder)
print(root.val, root.left.val, root.right.val)
