"""
Given an array of integers, find the maximum possible sum you can get from one
of its contiguous subarrays. The subarray from which this sum comes must contain
at least 1 element.

Example

For inputArray = [-2, 2, 5, -11, 6], the output should be
arrayMaxConsecutiveSum2(inputArray) = 7.

The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The maximum possible sum of a subarray within inputArray.
"""

from tools import timing

@timing
def arrayMaxConsecutiveSum2(inputArray):
    """
    docstring
    """
    max_so_far = inputArray[0]
    max_ending_here = inputArray[0]

    for i in range(1,len(inputArray)):
        max_ending_here = max(inputArray[i], max_ending_here + inputArray[i])
        max_so_far = max(max_so_far,max_ending_here)

    return max_so_far


# A Divide and Conquer based program
# for maximum subarray sum problem

# Find the maximum possible sum in
# arr[] such that arr[m] is part of it
def maxCrossingSum(arr, l, m, h) :
    # l: low, m: middle, h: high
    # Include elements on left of mid.
    sm = 0; left_sum = -10000

    for i in range(m, l-1, -1) :
        sm = sm + arr[i]

        if (sm > left_sum) :
            left_sum = sm


    # Include elements on right of mid
    sm = 0; right_sum = -10000
    for i in range(m + 1, h + 1) :
        sm = sm + arr[i]

        if (sm > right_sum) :
            right_sum = sm


    # Return sum of elements on left and right of mid
    return left_sum + right_sum;

@timing
# Returns sum of maxium sum subarray in aa[l..h]
def arrayMaxConsecutiveSum(arr, l, h) :

    # Base Case: Only one element
    if (l == h) :
        return arr[l]

    # Find middle point
    m = (l + h) // 2

    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #     subarray crosses the midpoint
    return max(arrayMaxConsecutiveSum(arr, l, m),
               arrayMaxConsecutiveSum(arr, m+1, h),
               maxCrossingSum(arr, l, m, h))





inputArray = [1, -2, 3, -4, 5, -3, 2, 2, 2]
assert arrayMaxConsecutiveSum2(inputArray) == 8
assert arrayMaxConsecutiveSum(inputArray, 0, len(inputArray)-1) == 8
