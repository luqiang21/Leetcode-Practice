"""
Given two strings A and B, find the minimum number of times A has to be repeated
such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring
of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
from tools import timing

class Solution:
    # mine solution, didn't figure out exact reason for n//m + 2
    @timing
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n = len(B)
        m = len(A)
        temp = A
        i = 1
        while i <= n // m + 2:
            if B in temp:
                return i
            i += 1
            temp = A*i
        return -1

    # from leetcode
    '''
    Intuition

    The question can be summarized as "What is the smallest k for which B is a
    substring of A * k?" We can just try every k.

    Algorithm

    Imagine we wrote S = A+A+A+.... If B is to be a substring of S, we only need
    to check whether some S[0:], S[1:], ..., S[len(A) - 1:] starts with B, as S
    is long enough to contain B, and S has period at most len(A).

    Now, suppose q is the least number for which len(B) <= len(A * q). We only
    need to check whether B is a substring of A * q or A * (q+1). If we try k < q,
     then B has larger length than A * q and therefore can't be a substring.
     When k = q+1, A * k is already big enough to try all positions for B; namely,
      A[i:i+len(B)] == B for i = 0, 1, ..., len(A) - 1.
    '''
    @timing
    def repeatedStringMatch1(self, A, B):
        q = (len(B) - 1) // len(A) + 1 # len(B) - 1 because at least one char is at the first A

        for i in range(2):
            if B in A*(q+i):
                return q+i

        return -1

sol = Solution()
A = "abcd"
B = "cdabcdab"
assert sol.repeatedStringMatch(A, B) == 3
assert sol.repeatedStringMatch1(A, B) == 3
