'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# my solution, accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len_1 = 0
        len_2 = 0
        num1 = 0
        num2 = 0

        while l1.next:
            num1 += 10**len_1 * l1.val
            len_1 += 1

            l1 = l1.next
        num1 += 10**len_1 * l1.val

        while l2.next:
            num2 += 10**len_2 * l2.val
            len_2 += 1
            l2 = l2.next
        num2 += 10**len_2 * l2.val

        print(num1, num2)

        ans = num1 + num2
        print(list(str(ans)))
        ans_list = list(str(ans))
        l3 = ListNode(int(ans_list[-1]))
        l = l3
        for i in range(len(ans_list) - 2, -1, -1):
            l.next = ListNode(int(ans_list[i]))
            l = l.next
        return l3

    # a good solution from others
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = l3 = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, num = divmod(v1 + v2 + carry, 10)
            l3.next = ListNode(num)
            l3 = l3.next

        return root.next
