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
from tools import timing


class Solution(object):
    # time limit exceeded using brute force
    @timing
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

    '''
    We iterate through every element. For every element arr[i],
    we find a pair with sum “-arr[i]”. This problem reduces to pairs sum and
    can be solved in O(n) time using hashing.

    Run a loop from i=0 to n-3
      Create an empty hash table
      Run inner loop from j=i+1 to n-1
          If -(arr[i] + arr[j]) is present in hash table
             print arr[i], arr[j] and -(arr[i]+arr[j])
          Else
             Insert arr[j] in hash table.
    '''

    @timing
    def threeSum2(self, nums):

        found = False
        answer = []
        n = len(nums)
        for i in range(n-2):
            # find all pairs with sum equals -nums[i]
            s = set()
            for j in range(i+1, n):
                x = nums[i] + nums[j]
                x = -x
                if x in s:
                    temp = sorted([nums[i], nums[j], x])
                    if temp not in answer:
                        answer.append(temp)
                    found = True
                else:
                    s.add(nums[j])
        if found == False:
            return None
        else:
            return answer


    '''
    1. Sort all element of array
    2. Run loop from i=0 to n-2.
         Initialize two index variables l=i+1 and r=n-1
    4. while (l < r)
         Check sum of arr[i], arr[l], arr[r] is
         zero or not if sum is zero then print the
         triplet and do l++ and r--.
    5. If sum is less than zero then l++
    6. If sum is greater than zero then r--
    7. If not exist in array then print not found.
    '''
    @timing
    def threeSum3(self, nums):

        # sort array elements
        nums.sort()
        answer = []
        n = len(nums)
        for i in range(0, n-2):

            # initialize left and right
            l = i + 1
            r = n - 1
            x = nums[i]
            while (l < r):

                if (x + nums[l] + nums[r] == 0):
                    # print elements if it's sum is zero
                    if [x, nums[l], nums[r]] not in answer:
                        answer.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1


                # If sum of three elements is less
                # than zero then increment in left
                elif (x + nums[l] + nums[r] < 0):
                    l += 1

                # if sum is greater than zero than
                # decrement in right side
                else:
                    r -= 1

        answer.sort(reverse=True)
        return answer


S = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum1(S))
print(sol.threeSum2(S))
print(sol.threeSum3(S))
