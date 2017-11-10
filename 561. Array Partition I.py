'''Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].'''

import time
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

class Solution:
    @timing
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort the array, and sum over all numbers in even position
        nums.sort()
        total = 0
        for i, num in enumerate(nums):
            if i%2 == 0:
                total += num
        print [(nums[i], nums[i+1]) for i in range(len(nums)) if i%2 == 0]
        return total

sol = Solution()
nums = [1, 4, 3, 2]
print(nums)
print(sol.arrayPairSum(nums))
print

nums = [10, 40, 30, 2, 1, 7]
print(nums)
print(sol.arrayPairSum(nums))
