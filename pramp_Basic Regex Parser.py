"""
Implement a regular expression function isMatch that supports the '.' and '*'
symbols. The function receives two strings - text and pattern - and should return
true if the text matches the pattern as a regular expression. For simplicity,
assume that the actual symbols '.' and '*' do not appear in the text string and
are used as special symbols only in the pattern string.

In case you aren’t familiar with regular expressions, the function determines
if the text and pattern are the equal, where the '.' is treated as a single a
character wildcard (see third example), and '*' is matched for a zero or more
sequence of the previous letter (see fourth and fifth examples). For more
information on regular expression matching, see the Regular Expression Wikipedia page.

Explain your algorithm, and analyze its time and space complexities.

Examples:

input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true
Constraints:

[time limit] 5000ms
[input] string text
[input] string pattern
[output] boolean
"""

from tools import timing

# recursive
@timing
def is_match(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (is_match(text, pattern[2:]) or
                first_match and is_match(text[1:], pattern))
    else:
        return first_match and is_match(text[1:], pattern[1:])

# DP, time: O(NM), space O(NM)
@timing
def is_match1(text, pattern):
    n, m = len(text), len(pattern)
    match = [[False for _ in range(m+1)] for _ in range(n+1)]

    match[0][0] = True # empty text and empty pattern matches

    # empty text and nonempty pattern
    for j in range(1, m+1):
        if j > 1 and pattern[j-1] == '*':
            match[0][j] = match[0][j-2]

    for i in range(1, n+1):
        for j in range(1, m+1):
            # if i-1 th text and j-1 th pattern match, or j-1 th pattern is a '.'
            if text[i-1] == pattern[j-1] or pattern[j-1] == '.':
                match[i][j] = match[i-1][j-1]
            elif j > 1 and pattern[j-1] == '*':
                # if the char before * matches at least once, i.e. equal char or
                # pattern is '.'
                # match[i][j-2] is for matching 0, cause we need to skip the last 2
                # characters in the pattern. match[i - 1][j] is for matching 1, cause
                # we need to skip 1 character in the string, but keep the entire pattern
                if pattern[j-2] == '.' or text[i-1] == pattern[j-2]:
                    match[i][j] = match[i][j-2] or match[i-1][j]

                # if doesn't match, the only way is 0 matched
                else:
                    match[i][j] = match[i][j-2]

    return match[n][m]

text = "acd"
pattern = "ab*c."
ans = True
assert is_match(text, pattern) == ans
assert is_match1(text, pattern) == ans
