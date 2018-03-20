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

text = "acd"
pattern = "ab*c."
ans = True
assert is_match(text, pattern) == ans
