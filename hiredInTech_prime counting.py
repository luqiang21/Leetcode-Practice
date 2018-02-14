'''
A classic math task is to count the prime numbers less than or equal to some
integer number N. In this task you have to write a function, which does this
for a given N, where 1 <= N <= 10^6. We don't count 1 a prime.

Here are a few examples:

For N=10, the prime numbers, which are less than or equal to 10 are: 2, 3, 5, 7.
The function must return 4. For N=31, the prime numbers are: 2, 3, 5, 7, 11, 13,
17, 19, 23, 29, 31. The function must return 11.
'''

from tools import timing
@timing
def prime_counting1(n):
    # Write your code here
    count = 0
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    return count

# complexity O(n loglogn)
@timing
def prime_counting(n):
    # Write your code here
    count = 0
    prime = [True for _ in range(n+1)]
    for i in range(2, n+1):
       if prime[i]:
           count += 1

           for j in range(i*i, n+1, i):
               prime[j] = False

    return count

n = 10
ans = 4
assert prime_counting1(n) == ans
assert prime_counting(n) == ans
n = 31
ans = 11
assert prime_counting1(n) == ans
assert prime_counting(n) == ans
