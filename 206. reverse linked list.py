"""
Reverse a linked List
"""


class Solution:
    # iterative way
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        current = head
        last = None
        while current:
            temp = current.next
            current.next = last
            last = current
            current = temp

        return last

    # recursive way
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        last = None
        current = head

        ans = self.reverse(current, last)
        return ans

    def reverse(self, current, last):
        if not current:
            return last
        else:
            temp = current.next
            current.next = last
            last = current
            current = temp

            return self.reverse(current, last)


    # recursive way, but go to the final node first, then get back
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head, None)

    def helper(self, current, last):
        if current:
            res = self.helper(current.next, current)
            current.next = last # change next
        else:
            res = last # only assign value for res here
        return res
