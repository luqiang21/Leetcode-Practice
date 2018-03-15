"""
Given a binary tree t, determine whether it is symmetric around its center, i.e.
each side mirrors the other.

Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
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
the output should be isTreeSymmetric(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be isTreeSymmetric(t) = false.

Here's what the tree in this example looks like:

    1
   / \
  2   2
   \   \
   3    3
As you can see, it is not symmetric.

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size < 5 · 104,
-1000 ≤ node value ≤ 1000.

[output] boolean

Return true if t is symmetric and false otherwise.


"""

# my solution
#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def inorder(t, res):

    if t.left:
        inorder(t.left, res)
    res.append(t.value)
    if t.right:
        inorder(t.right, res)

def inorder1(t):
    if t:
        return inorder(t.left)+[t.value]+inorder(t.right)
    return []

def isTreeSymmetric(t):
    if not t:
        return True

    if t.left and t.right:
        left = []
        right = []
        inorder(t.left, left)
        inorder(t.right, right)

        if len(left) != len(right):
            return False

        for i in range(len(left)):
            if left[i] != right[len(left) - 1 - i]:
                return False
        return True

    return False


# solution from others
def isTreeSymmetric(t):
    if t is None:
        return True
    return helper(t.left, t.right)

def helper(l, r):
    if l is None and r is None:
        return True
    if l is None or r is None:
        return False
    return (l.value == r.value) and helper(l.left, r.right) and helper(l.right, r.left)
