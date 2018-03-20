"""
Similar with pramp_smallest substring of all characters

Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty
string "".

If there are multiple such windows, you are guaranteed that there will always be
only one unique minimum window in S.

"""

from tools import timing

@timing
def minWindow(s, t):
        from collections import defaultdict
        dic = defaultdict(int)
        for ch in t:
            dic[ch] += 1

        start, end = 0, 0
        counter, min_start, min_end = len(t), 0, None

        while end < len(s):
            if dic[s[end]] > 0:
                # exist
                counter -= 1
            # decrease dic[s[end]], if not exist in t, it will be negative
            dic[s[end]] -= 1
            end += 1
            # print(s[end-1], dic[s[end-1]], start, end)
            # when we found a valid window, move start to find a smaller window
            while counter == 0:
                if not min_end or end - start < (min_end - min_start):
                    min_start, min_end = start, end
                dic[s[start]] += 1
                # removed s[start], if it is in t, then dic[s[start]] will be greater than 0
                if dic[s[start]] > 0:
                    # mismatch after remove start
                    counter += 1
                start += 1
                # print(start, counter, dic[s[start-1]], min_start, min_end)
        return s[min_start: min_end] if min_end != None else ""

s = "ab"
t = "a"
ans = "a"
assert minWindow(s, t) == ans

S = "ADOBECODEBANCC"
T = "ABCC"
ans = "BANCC"
assert minWindow(S, T) == ans
