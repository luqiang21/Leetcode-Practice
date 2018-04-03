"""

Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""
from tools import timing

class Solution:
    @timing
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        self.backtracking(sorted(candidates), target, res, temp, 0)
        return res

    def backtracking(self, candidates, target, res, temp, start):
        if target < 0:
            return
        elif target == 0:
            res.append(temp[:])
        else:
            for i in range(start, len(candidates)):
                num = candidates[i]
                temp.append(num)
                self.backtracking(candidates, target - num, res, temp, i)
                temp.pop()
    # avoid unnecessary steps
    @timing
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        self.backtracking1(sorted(candidates), target, res, temp, 0)
        return res

    def backtracking1(self, candidates, target, res, temp, start):
        if target == 0:
            res.append(temp[:])
        else:
            for i in range(start, len(candidates)):
                num = candidates[i]
                # if num is greater than target, no need to continue search since candidates are sorted.
                if num > target:
                    break
                temp.append(num)
                self.backtracking1(candidates, target - num, res, temp, i)
                temp.pop()  

candidates = [2, 3, 6, 7]
target = 7
ans = [[2, 2, 3], [7]]
assert Solution().combinationSum(candidates, target) == ans
assert Solution().combinationSum1(candidates, target) == ans
