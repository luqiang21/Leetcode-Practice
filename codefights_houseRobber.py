"""
You are planning to rob houses on a specific street, and you know that every house
on the street has a certain amount of money hidden. The only thing stopping you
from robbing all of them in one night is that adjacent houses on the street have
a connected security system. The system will automatically trigger an alarm if
two adjacent houses are broken into on the same night.

Given a list of non-negative integers nums representing the amount of money hidden
in each house, determine the maximum amount of money you can rob in one night
without triggering an alarm.

Example

For nums = [1, 1, 1], the output should be
houseRobber(nums) = 2.

The optimal way to get the most money in one night is to rob the first and the
third houses for a total of 2.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

An array representing the amount of money that each house on the street has.

Guaranteed constraints:
0 ≤ nums.length ≤ 100,
0 ≤ nums[i] ≤ 500.

[output] integer


"""

from tools import timing
@timing
def houseRobber(nums):
    mem = [0]*len(nums)
    if not nums:
        return 0
    if len(nums) < 2:
        return nums[0]
    mem[0] = nums[0]
    mem[1] = max(mem[0], nums[1])
    for i, n in enumerate(nums[2:], 2):
        mem[i] = max(mem[i-2]+nums[i], mem[i-1])
    return mem[len(nums)-1]

@timing
def houseRobber1(nums):
    a = b = 0
    for x in nums:
        a, b = b+x, max(a, b)
    return max(a, b)

nums = [213, 59, 76, 87, 209, 98, 94, 175, 249, 123, 109, 233, 199, 162, 51, 92, 146, 154, 146, 118, 183]
ans = 1711
assert houseRobber(nums) == ans
assert houseRobber1(nums) == ans
