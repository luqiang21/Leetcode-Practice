"""
Implement a program, which given an integer n, computes the sum of its digits.

If a negative number is given, the function should work as if it was positive.

For example, if n is 1325132435356, the digit's sum is 43. If n is -10, the sum is 1 + 0 = 1.

In the test cases for this task we will have that -2^63 < n < 2^63.

Test examples
Input	Output
10	      1
2	      2
-3456	  18
1325132435356	43
"""
from tools import timing

@timing
def digit_sum1(number):
    # Write your code here
    # go through digit in the number's string format
    number = abs(number)
    ans = 0
    for digit in str(number):
        ans += int(digit)
    return ans
@timing
def digit_sum(number):
    # Write your code here

    if number < 0:
        number = -1 * number
    ans = 0
    while number > 0:
        ans += number % 10
        number //= 10

    return ans

number, ans = 10, 1
assert digit_sum1(number) == ans
assert digit_sum(number) == ans

number, ans = 2, 2
assert digit_sum1(number) == ans
assert digit_sum(number) == ans

number, ans = -3456, 18
assert digit_sum1(number) == ans
assert digit_sum(number) == ans

number, ans = 1325132435356, 43
assert digit_sum1(number) == ans
assert digit_sum(number) == ans

print("All tests passed.")
