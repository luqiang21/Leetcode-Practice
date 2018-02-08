"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""

from tools import timing

class Solution:
    """
    We use an extra array in which we place every element of the array at its
    correct position i.e. the number at index ii in the original array is placed
    at the index (i+k)(i+k). Then, we copy the new array to the original one.
    """
    # Time complexity : O(n)O(n). One pass is used to put the numbers in the new array.
    # And another pass to copy the new array to the original one.
    # Space complexity : O(n)O(n). Another array of the same size is used.

    @timing
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = nums[:]
        for i in range(len(nums)):
            temp[(i + k) % len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = temp[i]


    """
    details refer https://leetcode.com/problems/rotate-array/solution/
    Approach #3 Using Cyclic Replacements [Accepted]

    """


    """
    This approach is based on the fact that when we rotate the array k times,
    k elements from the back end of the array come to the front and the rest of the
    elements from the front shift backwards.

    In this approach, we firstly reverse all the elements of the array. Then,
    reversing the first k elements followed by reversing the rest n−k elements
     gives us the required result.

    Let n=7 and k=3.

    Original List                   : 1 2 3 4 5 6 7
    After reversing all numbers     : 7 6 5 4 3 2 1
    After reversing first k numbers : 5 6 7 4 3 2 1
    After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
    """

    #Time complexity : O(n). nn elements are reversed a total of three times.
    #Space complexity : O(1). No extra space is used.
    @timing
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
print('original:', nums, 'k:', k)

sol.rotate1(nums, k)
print(nums)
nums = [1,2,3,4,5,6,7]
print('original:', nums, 'k:', k)
sol.rotate(nums, k)
print(nums)
