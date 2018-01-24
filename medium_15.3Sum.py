"""
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution(object):
    # time limit exceeded using brute force
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        n = len(nums)
        found = True
        for i in range(0, n-2):

            for j in range(i+1, n-1):

                for k in range(j+1, n):

                    if (nums[i] + nums[j] + nums[k] == 0):
                        temp = sorted([nums[i], nums[j], nums[k]])
                        if temp not in answer:
                            answer.append(temp)
                        found = True


        # If no triplet with 0 sum
        # found in array
        if (found == False):
            print(" not exist ")
            return None
        else:
            return sorted(answer, reverse=True)


S = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum1(S))
