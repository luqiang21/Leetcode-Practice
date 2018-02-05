"""
Given an array and a value, remove all instances of that value in-place and
return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""

from tools import timing

class Solution:
    @timing
    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        nums = nums[:i]
        # print("nums is", nums)
        return i

    @timing
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        # print("nums is", nums)
        return len(nums)

sol = Solution()
nums = [3, 2, 2, 3]
val = 3
assert sol.removeElement1(nums, val) == 2, sol.removeElement1(nums, val)
nums = [3, 2, 2, 3]
assert sol.removeElement(nums, val) == 2, sol.removeElement(nums, val)
print("test passed.")
