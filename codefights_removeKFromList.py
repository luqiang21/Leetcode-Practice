"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n
is the number of elements in the list, since this is what you'll be asked to do
during an interview.

Given a singly linked list of integers l and an integer k, remove all elements
from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer k

An integer.

Guaranteed constraints:
-1000 ≤ k ≤ 1000.

[output] linkedlist.integer

Return l with all the values equal to k removed.
"""
from tools import timing
# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

@timing
def removeKFromList1(l, k):
    if not l:
        return l
    dummy = ListNode(l.value)
    dummy.next = l

    current = l
    prev = dummy

    while current:
        if current.value == k:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    return dummy.next

@timing
def removeKFromList(l, k):
    cur = l
    while cur:
        if cur.next and cur.next.value == k:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return l.next if l and l.value == k else l

def printNode(head):
    while head:
        print(head.value,end=" ")
        head = head.next
    print()

n1 = ListNode(3)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

k = 3
printNode(n1)
head = removeKFromList1(n1, k)
printNode(head)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
printNode(n1)
head = removeKFromList(n1, k)
printNode(head)
