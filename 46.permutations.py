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

    # Iterative way
    """ the basic idea is, to permute n numbers, we can add the nth number into
    the resulting List<List<Integer>> from the n-1 numbers, in every possible position.

    For example, if the input num[] is {1,2,3}: First, add 1 into the initial
    List<List<Integer>> (let’s call it “answer”).

    Then, 2 can be added in front or after 1. So we have to copy the List in
    answer (it’s just {1}), add 2 in position 0 of {1}, then copy the original
    {1} again, and add 2 in position 1. Now we have an answer of {{2,1},{1,2}}.
    There are 2 lists in the current answer.

    Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0;
    then copy {2,1} and {1,2}, and add 3 into position 1, then do the same thing
    for position 3. Finally we have 2*3=6 lists in answer, which is what we want.
    """
    @timing
    def permute1(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms

     # corresponding recursive way
    @timing
    def permute2(self, nums):
        if len(nums) <= 1:
            return [nums]

        all_chars_except_last = nums[:-1]
        last = nums[-1]
        perms_all_chars_except_last = self.permute2(all_chars_except_last)

        perms = []
        for perm in perms_all_chars_except_last:
            for pos in range(len(all_chars_except_last)+1):
                perms.append(
                perm[:pos]
                + [last]
                + perm[pos:]
                )
        return perms



sol = Solution()
assert sol.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
assert sol.permute1([1,2,3]) == [[3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]]
assert sol.permute2([1,2,3]) == [[3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]]
