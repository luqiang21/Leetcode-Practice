"""
This is a classic task requiring you to count all integer factors of a positive
integer number N, including 1 and the number itself. Note that this is not just
about the prime factors but all of them.

For example for 12 there are 6 such factors: 1, 2, 3, 4, 6, 12.

In this task N will be in the range [1, 10^12].

Your function will receive one argument - the number N. It must return one integer
 - the number of all factors of N as described above.

Here is an example test case:

SAMPLE INPUT

12
SAMPLE OUTPUT

6
"""

from tools import timing

@timing
def count_numbers_factors(n):
    # Write your code here
    count = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if n//i != i:
                count += 2
            else:
                count += 1

    return count
assert count_numbers_factors(1) == 1
assert count_numbers_factors(2) == 2
assert count_numbers_factors(12) == 6

"""
Given an integer n, calculate the sum of all divisors of n.

For example, the divisors of 8 are 1,2,4 and 8 and 1 + 2 + 4 + 8 = 15
The divisors of 7 are 1 and 7, which makes the sum 8.

The input number n will be in the range [1, 10^9].

Return one number - the sum of divisors of n.

Sample test examples
Input	Output
8	15
7	8
1	1
1000	2340
"""
@timing
def sum_the_divisors(n):
    # Write your code here
    sum = 0
    for i in range(1, int(n**0.5 + 1)):
        if n%i == 0:
            if n//i == i:
                sum += i
            else:
                sum += i + n//i
    return sum

assert sum_the_divisors(8) == 15
assert sum_the_divisors(7) == 8
assert sum_the_divisors(1) == 1
assert sum_the_divisors(1000) == 2340
print('All tests passed.')
