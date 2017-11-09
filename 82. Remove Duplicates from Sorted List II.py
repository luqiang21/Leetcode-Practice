'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "None"
        else:
            return "{} --> {}".format(self.val, repr(self.next))


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head

        while cur:
            # if cur has next, and next's value is the same as cur's value
            if cur.next and cur.next.val == cur.val:
                val = cur.val
                # check future nodes
                while cur and cur.val == val:
                    cur = cur.next
                # assign non duplicate node
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return dummy.next







head, head.next, head.next.next = ListNode(1), ListNode(2), ListNode(2)
head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(4)
head.next.next.next.next.next, head.next.next.next.next.next.next = ListNode(5), ListNode(5)
print 'Before', head
print 'After remove', Solution().deleteDuplicates(head)
