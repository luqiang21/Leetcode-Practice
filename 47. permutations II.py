"""
Given a collection of numbers that might contain duplicates, return all possible
unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from tools import timing
class Solution:
    @timing
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        used = [False for _ in nums]
        self.backtracking(res, temp, sorted(nums), used)
        return res

    def backtracking(self, res, temp, nums, used):
        if len(temp) == len(nums):
            res.append(temp[:])
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                temp.append(nums[i])
                used[i] = True
                self.backtracking(res, temp, nums, used)
                used[i] = False
                temp.pop()

nums = [1, 1, 2]
ans = [
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
assert Solution().permuteUnique(nums) == ans
