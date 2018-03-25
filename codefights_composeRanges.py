"""
Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

Example

For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
composeRanges(nums) = ["-1->2", "6->7", "9"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

A sorted array of unique integers.

Guaranteed constraints:
0 ≤ nums.length ≤ 15,
-(231 - 1) ≤ nums[i] ≤ 231 - 1.

[output] array.string


"""
from tools import timing
@timing
def composeRanges(nums):
    if len(nums) < 1:
        return []

    res = []
    start = last = nums[0]
    for cur in (nums+[nums[-1]+2])[1:]:
        if cur - last > 1:
            if last != start:
                res.append(str(start)+"->"+str(last))
            else:
                res.append(str(last))
            start = cur

        last = cur
    return res


@timing
def composeRanges1(A):
    ans = []
    i = 0
    while i < len(A):
        j = i
        while j + 1 < len(A) and A[j+1] - A[j] == 1:
            j += 1
        if i == j:
            ans.append(str(A[i]))
        else:
            ans.append(str(A[i]) + '->' + str(A[j]))
        i = j + 1
    return ans


@timing
def composeRanges2(nums):
    ranges = []
    while nums:
        start = end = nums.pop(0)
        while nums and nums[0] - end == 1:
            end = nums.pop(0)
        ranges.append(str(start) + ("", "->" + str(end))[start != end])
    return ranges
nums = [-1, 0, 1, 2, 6, 7, 9]
ans = ["-1->2", "6->7", "9"]
assert composeRanges(nums) == ans
assert composeRanges1(nums) == ans
assert composeRanges2(nums) == ans
