"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""
from tools import timing
class Solution:
    @timing
    def frequencySort1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        # count
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        res = ""
        for c in sorted(count.values(), reverse=True):
            for key in count:
                if key not in res and count[key] == c:
                    for _ in range(c):
                        res += key

        return res

    @timing
    def frequencySort(self, s):
        letters = set(s)
        count_letter = [(s.count(l), l) for l in letters]
        count_letter.sort(reverse=True)
        res = ""

        for cl in count_letter:
            res += cl[0] * cl[1]
        return res

s = "Aabb"
ans = "bbAa"
ans1 = "bbaA"

assert Solution().frequencySort1(s) == ans or Solution().frequencySort1(s) == ans1
assert Solution().frequencySort(s) == ans or Solution().frequencySort(s) == ans1
