"""
Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

"""

from tools import timing

class Solution:
    @timing
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        temp = []
        idx = 1
        self.backtracking(res, temp, n, k, idx)

        return res

    def backtracking(self, res, temp, n, k, idx):
        if len(temp) == k and n == 0:
            res.append(temp[:])
            return

        for i in range(idx, 10):
            if i > n:
                continue
            temp.append(i)
            self.backtracking(res, temp, n - i, k, i + 1)
            temp.pop()

k, n = 3, 9
ans = [[1,2,6], [1,3,5], [2,3,4]]

assert Solution().combinationSum3(k, n) == ans
