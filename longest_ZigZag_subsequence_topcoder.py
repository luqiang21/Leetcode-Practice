"""
Longest Zig-Zag Subsequence
4
The longest Zig-Zag subsequence problem is to find length of the longest
subsequence of given sequence such that all elements of this are alternating.
If a sequence {x1, x2, .. xn} is alternating sequence then its element satisfy
 one of the following relation :

  x1 < x2 > x3 < x4 > x5 < …. xn or
  x1 > x2 < x3 > x4 < x5 > …. xn
Examples:

Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3

Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form
x1 < x2; or x1 > x2

Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest Zig-Zag of length 6.
"""
from tools import timing

class Solution(object):
    """docstring for Solution."""
    @timing
    def lzzs(self, a):
        bestLength = 1
        up = [1]
        down = [1]

        for i in range(1, len(nums)):
            up.append(1)
            down.append(1)

            for j in range(i):
                if a[i] > a[j]:
                    up[i] = max(down[j] + 1, up[i])

                if a[i] < a[j]:
                    down[i] = max(up[j] + 1, up[i])

            # bestLength = max(up[i], down[i], bestLength)
        bestLength = max(up[-1], down[-1])
        # print(up)
        # print(down)
        return bestLength



nums = [ 10, 22, 9, 33, 49, 50, 31, 60, 70 ]
ans = 6
sol = Solution()
assert sol.lzzs(nums) == ans, (sol.lzzs(nums),  ans)

nums = [1, 4, 5]
ans = 2
assert sol.lzzs(nums) == ans, (sol.lzzs(nums),  ans)

nums = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
ans = 8
assert sol.lzzs(nums) == ans, (sol.lzzs(nums),  ans)

print('test passed')
