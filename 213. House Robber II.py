"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place
for his thievery so that he will not get too much attention. This time, all houses
at this place are arranged in a circle. That means the first house is the neighbor
of the last one. Meanwhile, the security system for these houses remain the same
as for those in the previous street.

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
        # steal first one vs. steal last one
        res = max(self.helper(nums[1:]), self.helper(nums[:-1]))
        return res

    def helper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            max_.append(max(nums[i] + max_[i-2], max_[i-1]))
        return max_[-1]

nums = [1,2,3,4,5]
ans = 8
assert Solution().rob(nums) == ans
