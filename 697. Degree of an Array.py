"""

Given a non-empty array of non-negative integers nums, the degree of this array
is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of
nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

"""

from tools import timing

class Solution:
    @timing
    def findShortestSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mem = {}
        max_cnt = 0
        max_num = None
        for i, num in enumerate(nums):
            if num not in mem:
                cnt = 1
                mem[num] = [cnt, i, None]
            else:
                [cnt, low, _] = mem[num]
                cnt += 1
                mem[num] = [cnt, low, i]

            if cnt > max_cnt:
                max_num = num
                max_cnt = cnt
        res = float("inf")
        if mem[max_num][2] == None:
            return 1
        for num in mem:
            if mem[num][0] == max_cnt:
                length = mem[num][2] - mem[num][1]
                if length < res:
                    res = length
        return res + 1

    @timing
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
nums = [1, 2, 2, 3, 1]
assert Solution().findShortestSubArray1(nums) == 2
assert Solution().findShortestSubArray(nums) == 2
