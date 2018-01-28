'''
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

'''
from tools import timing

class Solution():
    # this solution is brute-force, O(n^2), time limit exceeded.
    @timing
    def reversePairs(self, nums):
        return sum([nums[j] > 2 * nums[i] for i in range(len(nums)) for j in range(0 , i)])


    # this solution modifies merge sort
    @timing
    def reversePairs1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, _ = self.mergeSort(nums)
        # print(_)
        return cnt

    def mergeSort(self, alist):
        count = 0
        leftcount = 0
        rightcount = 0
        blist = []

        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            # print('alist:', alist)
            # print('lefthalf:', lefthalf, 'righthalf:', righthalf)
            leftcount, lefthalf = self.mergeSort(lefthalf)
            rightcount, righthalf = self.mergeSort(righthalf)
            # print('leftcount', leftcount)
            # print('rightcount', rightcount)

            i = 0
            j = 0

            for ii in range(0, len(lefthalf)):
                jj = 0
                while jj < len(righthalf) and lefthalf[ii] > 2*righthalf[jj]:
                    count += 1#len(lefthalf[ii:])
                    jj += 1


            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] <= righthalf[j]:
                    blist.append(lefthalf[i])
                    i += 1
                else:
                    # if lefthalf[i] > 2*righthalf[j]:
                    #     count += len(lefthalf[i:]) # if leftHalf[i] is greater than rightHalf[j], then all numbers in leftHalf[i:] are greater than rightHalf[j]
                    blist.append(righthalf[j])
                    j += 1


            while i < len(lefthalf):
                blist.append(lefthalf[i])
                i += 1

            while j < len(righthalf):
                blist.append(righthalf[j])
                j += 1
        else:
            blist = alist[:]
        # print(blist)
        # print('count', count)
        # print('count + leftcount + rightcount',count + leftcount + rightcount)
        return count + leftcount + rightcount, blist

A = [1,3,2,3,1]
ans = 2
sol = Solution()
assert (sol.reversePairs(A) == ans), "Error"
assert (sol.reversePairs1(A) == ans), "Error"

A = [2,4,3,5,1]
ans = 3
assert (sol.reversePairs(A) == ans), "Error"
assert (sol.reversePairs1(A) == ans), "ERRor"
print("test passed")
