"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for
you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

"""

from tools import timing

class Solution:
    # Time complexity : O(n^2). Two loops of nn are there.

    # Space complexity : O(n). dp array of size n is used.
    @timing
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        up = [1 for _ in nums]
        up[0] = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if up[i] < up[j] + 1:
                        up[i] = up[j] + 1
        return max(up)

    # nlog(n), use binary search for inserting the subsequence
    @timing
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        tails = [0 for _ in nums]
        res = 0

        for num in nums:
            i, j = 0, res # i, j acted as start and end in binary search

            # try to insert number num into tails (the existing subsequence)
            while i != j:
                mid = (i + j) // 2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid

            tails[i] = num # either append, or replace a larger number at i position
            if i == res:
                res += 1

        return res

sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
assert sol.lengthOfLIS1(nums) == 4, "incorrect" + str(sol.lengthOfLIS1(nums))
assert sol.lengthOfLIS(nums) == 4, "incorrect" + str(sol.lengthOfLIS(nums))
print('All tests passed.')
