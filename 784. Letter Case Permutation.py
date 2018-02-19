'''
Given a string S, we can transform every letter individually to be lowercase or
uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
'''

from tools import timing


class Solution:
    @timing
    def letterCasePermutation1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 1:
            if S.isalpha():
                return [S.lower(), S.upper()]
            else:
                return [S]
        else:
            mid = len(S) // 2
            left = self.letterCasePermutation(S[:mid])
            right = self.letterCasePermutation(S[mid:])
            res = []
            for l in left:
                for r in right:
                    res.append(l + r)
        return res
    @timing
    def letterCasePermutation(self, S):
        if S == '':
            return ['']
        s = S[:1]
        if s.isalpha():
            upper = s.upper()
            lower = s.lower()
            permutations = self.letterCasePermutation(S[1:])
            arr = []
            for item in permutations:
                arr.append(upper + item)
                arr.append(lower + item)
        else:
            permutations = self.letterCasePermutation(S[1:])
            arr = []
            for item in permutations:
                arr.append(s + item)


        return arr
sol = Solution()

S = "a1b2"
ans = ["a1b2", "a1B2", "A1b2", "A1B2"]
print(sol.letterCasePermutation1(S))
print(sol.letterCasePermutation(S))

S = "3z4"
ans = ["3z4", "3Z4"]
print(sol.letterCasePermutation1(S))
print(sol.letterCasePermutation(S))

S = "12345"
ans = ["12345"]
print(sol.letterCasePermutation1(S))
print(sol.letterCasePermutation(S))
