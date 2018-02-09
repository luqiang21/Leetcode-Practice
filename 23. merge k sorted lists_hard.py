"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from queue import PriorityQueue
from tools import timing

class Solution:
    @timing
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodes = [] # store all node values
        head = point = ListNode(0)
        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next

        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next


    # using PriorityQueue
    @timing
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()

        for idx, l in enumerate(lists):
            if l:
                q.put((l.val, idx, l)) # add idx to avoid unordered

        while not q.empty():
            val, idx, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next

            if node:
                q.put((node.val, idx, node))

        return head.next

    # Convert merge k lists problem to merge 2 lists (k-1) times.
    def mergeTwoLists(self, l1, l2):
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

    # see explanation https://leetcode.com/problems/merge-k-sorted-lists/solution/
    @timing
    def mergeKLists3(self, lists):
        if len(lists) == 0:
            return None
        merged = lists[0]
        for l in lists[1:]:
            if l:
                merged = self.mergeTwoLists(l, merged)

        return merged

    @timing
    def mergeKLists(self, lists):
        amount = len(lists)

        interval = 1

        while interval < amount:
            for i in range(0, amount-interval, interval):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

l1 = [1, 2, 4]
l2 = [1, 3, 4]
l3 = [0, 9]
head1 = cur = ListNode(l1[0])
for i in l1[1:]:
    cur.next = ListNode(i)
    cur = cur.next

head2 = cur = ListNode(l2[0])
for i in l2[1:]:
    cur.next = ListNode(i)
    cur = cur.next

head3 = cur = ListNode(l3[0])
for i in l3[1:]:
    cur.next = ListNode(i)
    cur = cur.next
lists = [head1, head2, head3]

sol = Solution()
h1 = sol.mergeKLists1(lists)
h2 = sol.mergeKLists2(lists)
h3 = sol.mergeKLists3(lists)
h4 = sol.mergeKLists(lists)

lists1, lists2, lists3, lists4 = [], [], [], []
while h1:
    lists1.append(h1.val)
    h1 = h1.next
while h2:
    lists2.append(h2.val)
    h2 = h2.next
while h3:
    lists3.append(h3.val)
    h3 = h3.next
while h4:
    lists4.append(h4.val)
    h4 = h4.next
ans = [0, 1, 1, 2, 3, 4, 4, 9]
print('input:', l1, l2, l3)
assert lists1 == ans
assert lists2 == ans
assert lists3 == ans
assert lists4 == ans
print('return:', ans)
print("All tests passed.")
