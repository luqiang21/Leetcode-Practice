"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
 must be a substring, "pwke" is a subsequence and not a substring.

"""
from tools import timing


class Solution:
    @timing
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        max_len = 0
        for i, ch in enumerate(s):
            substring = ''
            for j, ch2 in enumerate(s[i:]):
                if ch2 not in substring:
                    substring += ch2
                else:
                    break

            if len(substring) > max_len:
                max_len = len(substring)


        return max_len


    @timing
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        last_seen = -1 # if not seen repeated character, use -1 to offset
        longest = 0

        for i, ch in enumerate(s):
            if ch in lookup:
                if last_seen < lookup[ch]:
                    # store the most recent repeated character's index
                    last_seen = lookup[ch]
            lookup[ch] = i
            length = i - last_seen
            if length > longest:
                longest = length
        return longest


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
sol = Solution()
assert sol.lengthOfLongestSubstring1(s1) == 3
assert sol.lengthOfLongestSubstring1(s2) == 1
assert sol.lengthOfLongestSubstring1(s3) == 3

assert sol.lengthOfLongestSubstring(s1) == 3
assert sol.lengthOfLongestSubstring(s2) == 1
assert sol.lengthOfLongestSubstring(s3) == 3

print('TEST passed.')
