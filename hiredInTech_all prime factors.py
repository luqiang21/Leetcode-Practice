"""
Given an integer N, for which 2 <= N <= 10^12, find its prime factors. The result
 must be a list of sorted prime numbers where each number is listed as many times
 as it is present in the prime decomposition of N.

Here are a few examples to make this clear:

For N=20 the prime decomposition is 20 = 2 * 2 * 5, so you must return 2, 2, 5.

For N=64 the prime decomposition is 64 = 2 * 2 * 2 * 2 * 2 * 2,
result must be 2, 2, 2, 2, 2, 2.

For N=1105 the prime decomposition is 1105 = 5 * 13 * 17,
result must be 5, 13, 17.

For N=9901 the prime decomposition consists of the number 9901 itself, so the
result must be a list with one element 9901 (9901 is a prime number).

You must write a function, which accepts one parameter - the number N and returns
the list of sorted prime numbers in the prime decomposition of N.
"""
from tools import timing

@timing
def all_prime_factors1(n):
    # Write your code here

    # Return a list with the prime decomposition numbers


    primes = []
    m = n
    for i in range(2, int(n**0.5)+2):
        # check if it is a prime number

        j = 2

        while m%i == 0:
            primes.append(i)
            m //= i
        if m == 1:
            break
    if m != 1:
        primes.append(m)
    return primes

@timing
def all_prime_factors(n):
    # Write your code here

    # Return a list with the prime decomposition numbers

    primes = []
    idx = 2
    while idx*idx <= n:
        while n%idx == 0:
            n //= idx
            primes.append(idx)
        idx += 1
    if n != 1:
        primes.append(n)
    return primes
N = 20
ans = [2, 2, 5]
assert all_prime_factors1(N) == ans
assert all_prime_factors(N) == ans

N = 64
ans = [2, 2, 2, 2, 2, 2]
assert all_prime_factors1(N) == ans
assert all_prime_factors(N) == ans
N = 1105
ans = [5, 13, 17]
assert all_prime_factors1(N) == ans
assert all_prime_factors(N) == ans
N = 9901
ans = [N]
assert all_prime_factors1(N) == ans
assert all_prime_factors(N) == ans
print('All tests passed.')
