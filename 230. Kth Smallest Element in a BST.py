"""
Given a binary search tree, write a function kthSmallest to find the kth smallest
element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find
the kth smallest frequently? How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
from tools import timing

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def size(self, root):
        if root is None:
            return 0
        return self.size(root.left) + 1 + self.size(root.right)

    @timing
    def kthSmallest1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return root

        left_size = self.size(root.left)

        if left_size + 1 == k:
            return root.val
        elif left_size + 1 > k:
            return self.kthSmallest1(root.left, k)
        else:
            return self.kthSmallest1(root.right, k - left_size - 1)

    @timing
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cur = root
        stack = []
        count = 0

        while len(stack) > 0 or cur:
            # go to leftmost
            while(cur):
                stack.append(cur)
                cur = cur.left

            tmp = stack.pop()
            count += 1
            if(count == k): return tmp.val
            cur = tmp.right

        return -1

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)

k = 2
assert Solution().kthSmallest1(root, k) == 3
assert Solution().kthSmallest(root, k) == 3
