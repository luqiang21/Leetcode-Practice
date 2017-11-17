'''Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''
from tools import timing
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

    @timing
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



class Solution2:
    # @param root, a TreeNode
    # @return a tree node
    def FindTwoNodes(self, root):
        if root:
            self.FindTwoNodes(root.left)

            if self.prev and self.prev.val > root.val:
                if self.n1 == None:
                    self.n1 = self.prev
                self.n2 = root
            self.prev = root
            self.FindTwoNodes(root.right)

    @timing
    def recoverTree(self, root):
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root


a = TreeNode(0)
a.left = TreeNode(1)
sol = Solution()

print(a.left.val, a.val)
sol.recoverTree(a)
print(a.left.val, a.val)
print()

a = TreeNode(0)
a.left = TreeNode(1)
sol2 = Solution2()

print(a.left.val, a.val)
sol2.recoverTree(a)
print(a.left.val, a.val)
