'''3 ways to solve Fibonacci problem'''
N = 20
import sys

import time
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

N = int(sys.argv[1])

# Approach 1: Recursion
# F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
'''This approach got an exponential time complexity, inefficient for large inputs.
F(n-2) and F(n-1) are calculated both using F(n) which is a repetitive work'''
time1 = time.time()
ans = fib(N) # 55
time2 = time.time()
print '%s function took %0.3f ms' % ("fib", (time2-time1)*1000.0)
print ans

# Approach 2: Dynamic Programming
# Store the Fibonacci numbers calculated so far and use them to calculate the next
# input in a single pass
@timing
def fib2(n):
    f = [0, 1]
    for i in xrange(2, n+1):
        fib_n = f[i-2] + f[-1]
        f.append(fib_n)
    return f[n]

print fib2(N)
'''Space complexity O(n), time complexity is O(n)'''

# Approach 3: Store the last two numbers
@timing
def fib3(n):
    if n == 1:return 1
    n1, n2, temp = 0, 1, 0
    for i in xrange(2, n+1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return temp
print fib3(1)
print fib3(2)
print fib3(N)
