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
    # complexity O((n-m+1)m), n = len(T), m = len(P)
    count = 0
    k = len(P)
    for i in range(len(T) - len(P) + 1):
        if T[i:i+k] == P:
            count += 1
    return count

@timing
def count1(T, P):
    # use Rabin-Karp, Processing time: theta(m), matching time: O((n-m+1)m),
    # based on certain assumptions, average-case running time is better
    count = 0

    n = len(T)
    m = len(P)
    d = 26
    q = 101
    h = d**(m-1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d*p + ord(P[i]))%q
        t = (d*t + ord(T[i]))%q

    for s in range(n-m+1):
        # print('substring', P, T[s:s+m])
        if p == t:
            if P == T[s:s+m]:
                count += 1
        if s < n-m:
            # print('adding', s+m, 'deleting', s)
            t = (d*(t - ord(T[s])*h) + ord(T[s+m])) % q
        # print(p, t)
    # print(count)
    return count


@timing
def count2(T, P):
    # use finite automata
    pass

@timing
def count3(T, P):
    # use KMP
    pass

T = 'babalabalabalatheend'
P = 'alabala'
assert count_brute_force(T, P) == 2
assert count1(T, P) == 2
T = "xxxxx"
P = "xx"
assert count_brute_force(T, P) == 4
assert count1(T, P) == 4
T, P = "3141592653589793", "26"
assert count_brute_force(T, P) == 1
assert count1(T, P) == 1
