'''
You are given two strings T and P. Write a program, which counts how many time P is found in T. If different occurrences of P in T overlap count each one of them.

Here is an example:

T = babalabalabalatheend P = alabala

The string P is found twice in T, first occurrence starts at position 4 (first letter is at position 1) and the second occurrence start at position 8.

Both strings will contain only lower-case latin letters (‘a’-’z’) and will have at least one letter. The maximum possible length for T is 100,000 and for P - 10,000.

The input is read from the standard input. The first line contains the string T and the second line contains the string P. The strings T and P will be such so that P does not occur in T more than 100 times. Try to think of a solution, which takes advantage of this.

The output is written to the standard output. It must contain only one integer number - the number of occurrences of P in T as described above.

SAMPLE INPUT

babalabalabalatheend
alabala
SAMPLE OUTPUT

2
'''
from tools import timing

@timing
def count_brute_force(T, P):
    count = 0
    k = len(P)
    for i in range(len(T) - len(P) + 1):
        if T[i:i+k] == P:
            count += 1
    return count

@timing
def count1(T, P):
    # use KMP


T = 'babalabalabalatheend'
P = 'alabala'
assert count_brute_force(T, P) == 2
