"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from tools import timing
class Solution:
    @timing
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = self.find_pivot_point(nums)
        if pivot == 0 or target < nums[0]:
            return self.binary(pivot, len(nums) - 1, nums, target)
        return self.binary(0, pivot - 1, nums, target)

    def find_pivot_point(self, nums):
        """
        Args: nums (list)
        Returns: pivot (int)
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid-1]:
                return mid
            elif nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        return 0

    def binary(self, left, right, nums, target):
        """
        Args: left, right, nums, target
        Returns: index (int)
        """
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


    @timing
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
nums = [4,5,6,7,0,1,2]
target = 0
assert Solution().search1(nums, target) == 4
assert Solution().search(nums, target) == 4
nums = [3, 1]
target = 1
assert Solution().search1(nums, target) == 1
assert Solution().search(nums, target) == 1
