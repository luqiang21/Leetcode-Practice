"""
Given a collection of candidate numbers (C) and a target number (T), find all
unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
from tools import timing

class Solution:
    @timing
    def combinationSum2(self, candidates, target):
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
        if target == 0:
            res.append(temp[:])
        else:
            for i in range(start, len(candidates)):
                num = candidates[i]
                # if num is greater than target, no need to continue search since candidates are sorted.
                if num > target:
                    break
                if i > start and candidates[i] == candidates[i-1]: # skip duplicates
                    continue
                temp.append(num)
                self.backtracking(candidates, target - num, res, temp, i+1)
                temp.pop()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
assert Solution().combinationSum2(candidates, target) == [[1,1,6],[1,2,5],[1,7],[2,6]]
