"""

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

"""
from tools import timing

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        right_node = head
        left_node = head
        for _ in range(n-1):
            if not right_node.next:
                return None
            right_node = right_node.next

        pre = None
        while right_node.next:
            pre = left_node
            left_node = left_node.next
            right_node = right_node.next

        if pre is None:
            return head.next
        pre.next = left_node.next
        return head

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n1.next.next.next = ListNode(4)
n1.next.next.next.next = ListNode(5)
root = Solution().removeNthFromEnd(n1, 2)
while root:
    print(root.val, end=" ")
    root = root.next
print()
