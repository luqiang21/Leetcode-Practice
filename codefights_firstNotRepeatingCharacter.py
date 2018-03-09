"""
Note: Write a solution that only iterates over the string once and uses O(1)
additional memory, since this is what you would be asked to do during a real interview.

Given a string s, find and return the first instance of a non-repeating character
in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since
it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

Guaranteed constraints:
1 ≤ s.length ≤ 105.

[output] char

The first non-repeating character in s, or '_' if there are no characters that do not repeat.


"""

from tools import timing
# iterate twice, time O(n), space O(n)
@timing
def firstNotRepeatingCharacter1(s):
    seen = dict()
    ans = '_'
    for ch in s:
        seen[ch] = seen.get(ch, 0) + 1
    for ch in s:
        if seen[ch] == 1:
            return ch

    return '_'

# iterate once, time O(n), space O(n)

@timing
def firstNotRepeatingCharacter(s):
    stack, unique = [], []
    for ch in s:
        if ch not in stack:
            stack.append(ch)
            unique.append(ch)
        elif ch in unique:
            unique.remove(ch)
    return unique[0] if unique else '_'

s = "abacabad"
ans = "c"
assert firstNotRepeatingCharacter1(s) == ans
assert firstNotRepeatingCharacter(s) == ans

s = "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"
ans = "d"
assert firstNotRepeatingCharacter1(s) == ans
assert firstNotRepeatingCharacter(s) == ans


s = "abacabaabacaba"
ans = "_"
assert firstNotRepeatingCharacter1(s) == ans
assert firstNotRepeatingCharacter(s) == ans
print("all tests passed.")
