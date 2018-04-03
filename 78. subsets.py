"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from tools import timing

class Solution:
    @timing
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.backtrack(res, [], nums, 0)
        return res

    def backtrack(self, res, templist, nums, start):
        res.append(templist[:])

        for i in range(start, len(nums)):

            templist.append(nums[i])
            self.backtrack(res, templist, nums, i+1)
            templist.pop()

    # iterative
    @timing
    def subsets1(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]

        return res


sol = Solution()
nums = [1, 2, 3]
ans = [
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3]
]
assert sol.subsets(nums) == ans
ans = [
  [],
  [1],
  [2],
  [1, 2],
  [3],
  [1, 3],
  [2, 3],
  [1, 2, 3]
]
assert sol.subsets1(nums) == ans
