"""
Given an integer array with all positive numbers and no duplicates, find the
number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

"""

from tools import timing

class Solution:
    @timing
    # recursive, time limit exceeded
    def combinationSum4_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        if target == 0:
            return 1

        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.combinationSum4_1(nums, target - nums[i])
        return res
    @timing
    # top down using memory
    def combinationSum4_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1] * (target + 1)
        dp[0] = 1
        return self.helper(dp, nums, target)

    def helper(self, dp, nums, target):
        if dp[target] != -1:
            return dp[target]

        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.helper(dp, nums, target - nums[i])
        dp[target] = res
        return res
    @timing
    # bottom up
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in sorted(nums):
                if i < num: break
                dp[i] += dp[i - num]
        return dp[-1]

nums = [1, 2, 3]
target = 4
assert Solution().combinationSum4_1(nums, target) == 7
assert Solution().combinationSum4_2(nums, target) == 7
assert Solution().combinationSum4(nums, target) == 7
