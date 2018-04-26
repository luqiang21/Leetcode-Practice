"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.
"""

from tools import timing

class Solution:
    @timing
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        max_ending_here = nums[0]

        # go through 1 to len(nums) - 1
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            max_sum = max(max_sum, max_ending_here)
        return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = 6
assert Solution().maxSubArray(nums) == ans
