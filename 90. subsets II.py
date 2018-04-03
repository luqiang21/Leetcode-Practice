"""
Given a collection of integers that might contain duplicates, nums, return all
possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""
from tools import timing

class Solution:
    @timing
    def subsetsWithDup1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        start = 0
        self.backtracking(res, temp, sorted(nums), start)
        return res

    def backtracking(self, res, temp, nums, start):
        if temp not in res:
            res.append(temp[:])

        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtracking(res, temp, nums, i + 1)
            temp.pop()

    @timing
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = [[]]
        for num in sorted(nums):
            for item in res[:]:
                temp = item + [num]
                if temp not in res:
                    res.append(temp)

        return res

nums = [1, 2, 2]
ans = [
  [],
  [1],
  [1, 2],
  [1, 2, 2],
  [2],
  [2, 2]
]
sol = Solution()
assert sol.subsetsWithDup1(nums) == ans
ans = [
  [],
  [1],
  [2],
  [1, 2],
  [2, 2],
  [1, 2, 2]
]
assert sol.subsetsWithDup(nums) == ans
