"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without alerting
the police.

"""
from tools import timing

class Solution:
    @timing
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        max_ = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            max_.append(max(nums[i] + max_[i-2], max_[i-1]))
        return max_[-1]

nums = [2,1,4,5]
ans = 7
assert Solution().rob(nums) == ans
