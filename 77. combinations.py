"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from tools import timing

class Solution:
    @timing
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        idx = 1
        self.backtracking(res, temp, n, k, idx)

        return res

    def backtracking(self, res, temp, n, k, idx):
        if k == 0:
            res.append(temp[:])
            return

        for i in range(idx, n + 1):
            temp.append(i)
            self.backtracking(res, temp, n, k - 1, i + 1)
            temp.pop()

n = 4
k = 2
ans = [
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4]]
assert Solution().combine(n, k) == ans
