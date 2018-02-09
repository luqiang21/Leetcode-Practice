"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from tools import timing
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    @timing
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2

        head = point = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                point.next = ListNode(l2.val)
                l2 = l2.next
            else:
                point.next = ListNode(l1.val)
                l1 = l1.next

            point = point.next
        point.next = l1 or l2
        return head.next

    # using recursion
    @timing
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        temp = None

        if l1.val < l2.val:
            temp = l1
            temp.next = self.mergeTwoLists(l1.next, l2)
        else:
            temp = l2
            temp.next = self.mergeTwoLists(l1, l2.next)
        return temp

l1 = [1,2,4]
l2 = [1,3,4]
head1 = cur = ListNode(l1[0])
for i in l1[1:]:
    cur.next = ListNode(i)
    cur = cur.next
head2 = cur = ListNode(l2[0])
for i in l2[1:]:
    cur.next = ListNode(i)
    cur = cur.next

sol = Solution()
h1 = sol.mergeTwoLists1(head1, head2)
list1 = []
while h1:
    list1.append(h1.val)
    h1 = h1.next
assert list1 == [1,1,2,3,4,4]

list2 = []
head2 = sol.mergeTwoLists(head1, head2)
while head2:
    list2.append(head2.val)
    head2 = head2.next
assert list2 == [1,1,2,3,4,4]
print('Tests passed.')
