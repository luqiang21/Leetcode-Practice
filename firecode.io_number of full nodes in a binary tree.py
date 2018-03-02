'''
Write a function to recursively/iteratively determine the total number of "full nodes"
in a binary tree.
A full node contains left and right child nodes.
If there are no full nodes, return 0.

Example:

       1
      / \
     2   3
    / \ / \
   4  5 6  7
  / \
 8   9

Full nodes count ==> 4
'''


class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        
class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    # Required collection modules have already been imported.
    # recursively
    def number_of_full_nodes1(self,root):
        if not root:
            return 0
        if not root.left_child or not root.right_child:
            return 0
        if root.left_child and root.right_child:
            return 1 + self.number_of_full_nodes(root.left_child) + self.number_of_full_nodes(root.right_child)
    # iteratively
    def number_of_full_nodes(self,root):
        queue = deque()
        if root:
            queue.append(root)
        cnt = 0

        while queue:
            node = queue.popleft()
            if node.left_child and node.right_child:
                cnt += 1
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)
        return cnt
