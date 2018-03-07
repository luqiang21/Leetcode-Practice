"""
Given a
Binary Search Tree
and an integer k, implement a method to find and return it's kth largest node

Example:
       4
      / \
     2   8
        / \
       5  10

K = 2, Output = 8 (TreeNode)

Note: Each node of BinaryTree is represented by a TreeNode. Your method must return TreeNode
"""

'''
The key here is to find the size of the right subtree at each node. If the
right_size + 1 is equal to k, return that node.

1. If root is None then, return None.
2. If root is not None then find the the size of the right subtree of this node.
3. if this right_size + 1 is equal to k then return this node.
4. If k is less than right size then recurse with root.right_child i.e. return
find_kth_largest(root.right_child, k)
5. Else, recurse through the left subtree with left node and k - right_size - 1.
i.e. return find_kth_largest(root.left_child, k - right_size - 1)

'''

class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' %self.data


class BinaryTree:

    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    # Helper Method
    def size(self,root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child))

    def find_kth_largest(self,root,k):
        # Return Element should be of type TreeNode
        if not root:
            return None

        right_size = self.size(root.right_child)
        if right_size + 1 == k:
            return root
        elif k <= right_size:
            return self.find_kth_largest(root.right_child, k)
        else:
            return self.find_kth_largest(root.left_child, k - right_size - 1)


root = TreeNode(5)
n4 = TreeNode(4)
n8 = TreeNode(8)
n2 = TreeNode(2)
n3 = TreeNode(3)
n7 = TreeNode(7)
n10 = TreeNode(10)
root.left_child = n4
root.right_child = n8
n4.left_child = n2
n4.right_child = n3
n8.left_child = n7
n8.right_child = n10

tree = BinaryTree(root_node=root)
k = 4
assert tree.find_kth_largest(root, k) == root, tree.find_kth_largest(root, k)
print("The {}th largest node is {}".format(k, tree.find_kth_largest(root, k)))
