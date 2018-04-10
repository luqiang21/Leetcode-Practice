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

inputArray = [1, -2, 3, -4, 5, -3, 2, 2, 2]
assert arrayMaxConsecutiveSum2(inputArray) == 8
