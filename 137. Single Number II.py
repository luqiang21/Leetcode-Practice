"""
Given an array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

"""
from tools import timing

class Solution:
    @timing
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*sum(set(nums)) - sum(nums)) // 2

   # Python3 code to find the element
    # that occur only once
    # not working for negative values if not handled
    @timing
    def singleNumber2(self, arr) :
        n = len(arr)
        # Initialize result
        result = 0
        INT_SIZE = 32
        # Iterate through every bit
        for i in range(0, INT_SIZE) :

            # Find sum of set bits
            # at ith position in all
            # array elements
            sm = 0
            x = (1 << i)
            for j in range(0, n) :
                if (arr[j] & x) :
                    sm = sm + 1

            # The bits with sum not
            # multiple of 3, are the
            # bits of element with
            # single occurrence.
            if (sm % 3) :
                if i == 31:
                    result -= 1 << 31
                else:
                    result = result | x

        return result
    @timing
    def singleNumber(self, nums):
        ones, twos = 0, 0

        for n in nums:
            # get numbers appear twice
            twos |= ones & n
            # get numbers appear once
            ones ^= n

            not_three = ~(ones & twos)
            # remove threes from ones and twos
            ones &= not_three
            twos &= not_three
        return ones

nums = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
sol = Solution()
assert sol.singleNumber1(nums) == 2
assert sol.singleNumber2(nums) == 2
assert sol.singleNumber(nums) == 2
