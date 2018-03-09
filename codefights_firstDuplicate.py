"""
Note: Write a solution with O(n) time complexity and O(1) additional space
complexity, since this is what you would be asked to do during a real interview.

Given an array a that contains only numbers in the range from 1 to a.length,
find the first duplicate number for which the second occurrence has the minimal
index. In other words, if there are more than 1 duplicated numbers, return the
number for which the second occurrence has a smaller index than the second
occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 3, 3, 1, 5, 2], the output should be
firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller
index than than second occurrence of 2 does, so the answer is 3.

For a = [2, 4, 3, 5, 1], the output should be
firstDuplicate(a) = -1.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ a.length.

[output] integer

The element in a that occurs in the array more than once and has the minimal index
for its second occurrence. If there are no such elements, return -1.
"""

from tools import timing
# time O(n), space O(n)
@timing
def firstDuplicate(a):
    s = set()
    res = -1
    for i in a:
        if i in s:
            res = i
            break
        s.add(i)
    return res

# time O(n), space O(1)
@timing
def firstDuplicate1(a):
    # mark the corresponding position, if mark twice, it should be positive
    for num in a:
        a[abs(num)-1] *= -1
        if a[abs(num)-1] > 0:
            return abs(num)
    return -1


a = [2, 3, 3, 1, 5, 2]
ans = 3
assert firstDuplicate(a) == ans
assert firstDuplicate1(a) == ans


a = [10, 6, 8, 4, 9, 1, 7, 2, 5, 3]
ans = -1
assert firstDuplicate(a) == ans
assert firstDuplicate1(a) == ans

a = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
ans = 6
assert firstDuplicate(a) == ans
assert firstDuplicate1(a) == ans
print("all tests passed.")
