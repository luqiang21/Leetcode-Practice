"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

"""
from tools import timing
class Solution:
    @timing
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return nums

        lower, upper = nums[0], nums[0]
        res = []
        nums.append(nums[-1]+1000)
        for i in range(1, len(nums)):
            if nums[i] - upper > 1:
                if upper == lower:
                    res.append(str(upper))
                else:
                    res.append(str(lower) + "->" + str(upper))
                lower, upper = nums[i], nums[i]
            else:
                upper = nums[i]
        return res
assert Solution().summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
