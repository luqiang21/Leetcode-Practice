'''
566. Reshape the Matrix My SubmissionsBack To Contest
User Accepted: 801
User Tried: 835
Total Accepted: 862
Total Submissions: 1206
Difficulty: Easy
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is an 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nOfElements = len(nums) * len(nums[0])
        if nOfElements != r * c:
            return nums
        else:
            rowTraversing = []
            for num in nums:
                for ele in num:
                    rowTraversing.append(ele)

            newList = []
            tem = []
            t = 0
            if r == 1:
                return rowTraversing
            for i in range(len(rowTraversing)):

                if t < c:
                    tem.append(rowTraversing[i])
                    t += 1

                else:
                    newList.append(tem)
                    tem = []
                    t = 0

        return newList
nums =[[1,2], [3,4]]
r = 1
c = 4
solution = Solution()
print(solution.matrixReshape(nums, r, c))


r = 2
c = 4
print(solution.matrixReshape(nums, r, c))
