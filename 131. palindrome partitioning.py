"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

"""
from tools import timing

class Solution:
    @timing
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        temp = []
        self.backtracking(res, temp, s, 0)
        return res

    def backtracking(self, res, temp, s, start):
        if start == len(s):
            res.append(temp[:])

        for i in range(start, len(s)):
            if not self.isPalindrome(s[start:i+1]):
                continue
            temp.append(s[start:i+1])
            self.backtracking(res, temp, s, i + 1)
            temp.pop()

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
