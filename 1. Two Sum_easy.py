"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from tools import timing

class Solution:
    # brute force
    @timing
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums[:-1]):
            for j, num2 in enumerate(nums[i+1:], i+1):
                if num1 + num2 == target:
                    return [i, j]

        return None

    # two-pass hash table
    @timing
    def twoSum2(self, nums, target):
        complements = {}
        for i, num in enumerate(nums):
            complements[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements and complements[complement] != i:
                return sorted([complements[complement], i])
        return None


    # One-pass Hash Table
    @timing
    def twoSum(self, nums, target):
        complements = {}
        for i, num in enumerate(nums):
            # print(i, num)
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i
            # print(complement, complements)
        return None


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
assert sol.twoSum1(nums, target) == [0, 1]
assert sol.twoSum2(nums, target) == [0, 1]
assert sol.twoSum(nums, target) == [0, 1]

print('Test passed')
