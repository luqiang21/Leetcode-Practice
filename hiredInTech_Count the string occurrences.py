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
def count1(T, P, d):
    # use Rabin-Karp, Processing time: theta(m), matching time: O((n-m+1)m),
    # based on certain assumptions, average-case running time is better
    count = 0

    n = len(T)
    m = len(P)
    # d = 26
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


'''Finite automat'''
# https://www.geeksforgeeks.org/searching-for-patterns-set-5-finite-automata/
NO_OF_CHARS = 256

def getNextState(pat, M, state, x):
    '''
    calculate the next state
    '''

    # If the character c is same as next character
      # in pattern, then simply increment state

    if state < M and x == ord(pat[state]):
        return state+1

    i = 0
    # ns stores the result which is next state

    # ns finally contains the longest prefix
     # which is also suffix in "pat[0..state-1]c"

     # Start from the largest possible value and
      # stop when you find a prefix which is also suffix
    for ns in range(state,0,-1):
        if ord(pat[ns-1]) == x:
            while(i < ns-1):
                if pat[i] != pat[state-ns+1+i]:
                    break
                i += 1
            if i == ns-1:
                return ns
    return 0

def computeTF(pat, M):
    '''
    This function builds the TF table which
    represents Finite Automata for a given pattern
    '''
    global NO_OF_CHARS

    TF = [[0 for i in range(NO_OF_CHARS)]\
          for _ in range(M+1)]

    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z

    return TF
@timing
def count2(pat, txt):
    # Python program for Finite Automata
    # Pattern searching Algorithm

    '''
    Prints all occurrences of pat in txt
    '''
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)

    count = 0
    # Process txt over FA.
    state=0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            count += 1
            print("     Pattern found at index: {}".\
                   format(i-M+1))
    return count

# KMPSearch
def computeLPS(P, m, lps):
    # lps[0] is 0
    i = 1
    l = 0 # length of previous longest prefix suffix
    # update lps[1:m-1]
    while i < m:
        if P[i] == P[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
                # we are not updating i here
            else:
                lps[i] = 0
                i += 1


@timing
def KMPSearch(P, T):
    # use KMP
    n = len(T)
    m = len(P)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*m
    j = 0 # index for P[]

    computeLPS(P, m, lps)
    # print(lps)
    cnt = 0
    i = 0
    while i < n:
        if T[i] == P[j]:
            i += 1
            j += 1

        if j == m:
            print("pattern found at shift", i-j)
            cnt += 1
            j = lps[j-1]

        # mismatch after j matches
        elif i < n and T[i] != P[j]:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
    return cnt

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(KMPSearch(pat, txt))


T = 'babalabalabalatheend'
P = 'alabala'
assert count_brute_force(T, P) == 2
assert count1(T, P, 26) == 2
assert count2(P, T) == 2, count2(T, P)
assert KMPSearch(P, T) == 2, KMPSearch(P, T)
print()
T = "xxxxx"
P = "xx"
assert count_brute_force(T, P) == 4
assert count1(T, P, 26) == 4
assert count2(P, T) == 4
assert KMPSearch(P, T) == 4, KMPSearch(P, T)


print()
T, P = "3141592653589793", "26"
assert count_brute_force(T, P) == 1
assert count1(T, P, 10) == 1
assert count2(P, T) == 1
assert KMPSearch(P, T) == 1, KMPSearch(P, T)
