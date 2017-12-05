"""
Re-ID
=====

Help the Commander assign these IDs by writing a function answer(n) which takes
 in the starting index n of Lambda's string of all primes, and returns the next
 five digits in the string. Commander Lambda has a lot of minions, so the value
 of n will always be between 0 and 10000.


Inputs:
    (int) n = 0
Output:
    (string) "23571"

Inputs:
    (int) n = 3
Output:
    (string) "71113"

"""
from tools import timing

@timing
def answer(n):
    # your code here
    if n < 0:
        return None

    s = '235711'
    prime_last = 11

    while len(s) < n + 5:
        num = prime_last + 1
        # find next prime number
        while True:
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                break
            num += 1

        s += str(num)
        prime_last = num

    return s[n:n+5]


print(answer(0)) # '23571'
print(answer(3)) # '71113'

'''amazingly, I solved this one within 25 min'''
