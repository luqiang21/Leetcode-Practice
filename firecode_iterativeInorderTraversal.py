"""
Given a binary tree, implement a method to perform the inorder traversal
iteratively and add the data of each node in a list in the way inorder traversal
is printed. Return an empty list in case of an empty tree.

Example:
     1
    / \
   2   3     ==> 4251637
  / \ / \
 4  5 6  7
"""
class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    # mine first solution
    def inorder_iterative1(self):
        inorder_list = []
        current = self
        stack = [current]
        while stack:
            current = stack.pop()

            while current.left_child and current.left_child not in inorder_list:
                stack.append(current)
                current = current.left_child

            inorder_list.append(current)

            if current.right_child:
                stack.append(current.right_child)
                
        return inorder_list

    # better solution from others
    def inorder_iterative(self):
        inorder_list = []
        stack = []
        current = self

        while stack or current:
            if current:
                stack.append(current)
                current = current.left_child

            else:
                node = stack.pop()
                inorder_list.append(node.data)
                current = node.right_child

        return inorder_list



    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data
