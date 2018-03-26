"""
We're going to store numbers in a tree. Each node in this tree will store a
single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

Given a binary tree t, find the sum of all the numbers encoded in it.

Example

For
t = {
    "value": 1,
    "left": {
        "value": 0,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": null,
        "right": null
    }
}
the output should be
digitTreeSum(t) = 218.
There are 3 numbers encoded in this tree:

Path 1->0->3 encodes 103
Path 1->0->1 encodes 101
Path 1->4 encodes 14
and their sum is 103 + 101 + 14 = 218.
t = {
    "value": 0,
    "left": {
        "value": 9,
        "left": null,
        "right": null
    },
    "right": {
        "value": 9,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be
digitTreeSum(t) = 193.
Because 09 + 091 + 093 = 193

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers. It's guaranteed that the sum of encoded integers won't exceed 252.

Guaranteed constraints:
1 ≤ tree size ≤ 2000,
1 ≤ tree depth ≤ 9,
0 ≤ node value ≤ 9.

[output] integer64

The sum of the integers encoded in t, as described above.
"""

from tools import timing

#
# Definition for binary tree:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

@timing
def digitTreeSum1(t):
    if not t:
        return 0
    nums = []
    dfs1(t, "", nums)
    return sum(nums)


def dfs1(t, temp_num, nums):
    # print(t.value, temp_num)
    if not t:
        return
    temp_num += str(t.value)

    if not t.left and not t.right:
        if temp_num:
            nums.append(int(temp_num))
    if t.left:
        dfs1(t.left, temp_num, nums)
    if t.right:
        dfs1(t.right, temp_num, nums)
@timing
def digitTreeSum(t):
    if not t:
        return 0

    ans = dfs(t, "", 0)
    return ans


def dfs(t, temp_num, ans):
    if not t:
        return ans
    temp_num += str(t.value)

    if not t.left and not t.right:
        if temp_num:
            ans += int(temp_num)
    if t.left:
        ans = dfs(t.left, temp_num, ans)
    if t.right:
        ans = dfs(t.right, temp_num, ans)

    return ans
n0 = Tree(0)
n1 = Tree(9)
n2 = Tree(9)
n3 = Tree(1)
n4 = Tree(3)
n0.left = n1
n0.right = n2
n2.left = n3
n2.right = n4

assert digitTreeSum1(n0) == 193
assert digitTreeSum(n0) == 193
