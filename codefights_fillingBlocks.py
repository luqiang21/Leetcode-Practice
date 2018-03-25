"""
You have a block with the dimensions 4 × n. Find the number of different ways you
can fill this block with smaller blocks that have the dimensions 1 × 2. You are
allowed to rotate the smaller blocks.

Example

For n = 1, the output should be
fillingBlocks(n) = 1.

There is only one possible way to arrange the smaller 1 × 2 blocks inside the
4 × 1 block.

For n = 4, the output should be
fillingBlocks(n) = 36.

Here are the 36 possible configuration of smaller blocks inside the 4 × 4 block:


Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 21.

[output] integer

An integer representing the number of possible configurations of smaller blocks
within the larger block.

"""
from tools import timing
@timing # solution https://stackoverflow.com/questions/31354624/number-of-ways-to-tile-a-w-x-h-grid-with-2-x-1-and-1-x-2-dominos
def fillingBlocks(n):
    return count_tilings(4, n)
memo = {}


def count_tilings_recursive(uncovered):
    if len(uncovered) & 1:
        return 0
    if not uncovered:
        return 1
    if uncovered not in memo:
        i, j = min(uncovered)
        memo[uncovered] = count_tilings_recursive(uncovered - {(i, j), (i, j + 1)}) \
                    + count_tilings_recursive(uncovered - {(i, j), (i + 1, j)})
    return memo[uncovered]


def count_tilings(m, n):
    return count_tilings_recursive(frozenset((i, j) for i in range(max(m, n)) for j in range(min(m, n))))




# solution from others on codefights
@timing
def fillingBlocks1(n):

    # Following https://cs.stackexchange.com/questions/42170/why-do-these-recurrences-determine-the-number-of-ways-of-tiling-a-3xn-rectangle
    # http://www.algorithmist.com/index.php/UVa_10918

    # This helped with deriving it:
    # How many ways can we fill the n-th column?
    # Make a tree where, at each step, we place a block horizontally or vertically
    # at the topmost empty position in the n-th column.
    # Find all the "leaves". The recurrence is:
    # f[n] = sum of the leaves
    # The subproblems blocks are the remaining shapes in each leaf.
    # To get their recurrence equation, make a tree using the same method...

    # following helps a lot
    # https://web.stanford.edu/class/cs97si/04-dynamic-programming.pdf

    # starts at n = [1,2]
    f = [1, 5]  # of ways to tile 4xn rectangle

    # subproblems
    a = [1, 2]  # of ways to tile with top/bottom two squares of column n removed
    # example of n = 4
    # ooox
    # ooox
    # oooo
    # oooo
    b = [1, 1]  # top and bottom squares of column n removed
    # example
    # ooox
    # oooo
    # oooo
    # ooox
    # g1 = [1, 2]
    # g2 = [0, 1]

    for _ in range(3,n+1):

        an = f[-1] + a[-1]
        bn = f[-1] + b[-2]

        fn = f[-2] + f[-1] + 2*a[-1] + b[-1]

        f += [fn]
        a += [an]
        b += [bn]

    return f[n-1]
n = 4
ans = 36
assert fillingBlocks(n) == ans
assert fillingBlocks1(n) == ans

n = 15
ans = 3335651
assert fillingBlocks(n) == ans
assert fillingBlocks1(n) == ans
