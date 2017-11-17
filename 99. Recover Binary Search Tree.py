'''Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, listv, listp):
        if root:
            self.inorder(root.left, listv, listp)
            listv.append(root.val); listp.append(root)
            self.inorder(root.right, listv, listp)
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        listv = [] # store values
        listp = [] # store nodes
        self.inorder(root, listv, listp)
        listv.sort()
        for i in range(len(listv)):
            listp[i].val = listv[i]

a = TreeNode(1)
a.left = TreeNode(0)
sol = Solution()

print(a.left.val, a.val)
sol.recoverTree(a)
print(a.left.val, a.val)
