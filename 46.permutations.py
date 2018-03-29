"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

from tools import timing

class Solution:
    @timing
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(res, [], nums)
        return res

    def backtrack(self, res, templist, nums):

        if len(templist) == len(nums):
            res.append(templist[:])
        else:
            for i in range(len(nums)):
                if nums[i] in templist:
                    continue
                templist.append(nums[i])
                self.backtrack(res, templist, nums)
                templist.pop()




sol = Solution()
assert sol.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
