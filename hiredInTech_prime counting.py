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
        if i!=2 and i%2 == 0:
            is_prime = False
        for j in range(3, int(i**0.5)+1, 2):
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
assert prime_counting1(n) == ans, (prime_counting1(n),ans)
assert prime_counting(n) == ans
n = 31
ans = 11
assert prime_counting1(n) == ans
assert prime_counting(n) == ans


@timing
def isPrime(n):

    # Corner case
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;

    return True
'''
Optimized School Method
We can do following optimizations:

Instead of checking till n, we can check till √n because a larger factor of n
must be a multiple of smaller factor that has been already checked.
The algorithm can be improved further by observing that all primes are of the
form 6k ± 1, with the exception of 2 and 3. This is because all integers can
be expressed as (6k + i) for some integer k and for i = ?1, 0, 1, 2, 3, or 4;
2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3). So a more efficient
method is to test if n is divisible by 2 or 3, then to check through all the
numbers of form 6k ± 1. (Source: wikipedia)
Below is the implementation of this solution.
'''

@timing
def isPrime1(n) :
    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

assert isPrime(11) == True

assert isPrime1(11) == True
assert isPrime(15) == False
assert isPrime1(15) == False
assert isPrime(1000003) == True
assert isPrime1(1000003) == True
