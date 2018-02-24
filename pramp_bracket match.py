'''
A string of brackets is considered correctly matched if every opening bracket in
the string can be paired up with a later closing bracket, and vice versa. For
instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance,
 “((” could become correctly matched by adding two closing brackets at the end,
 so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that
takes a bracket string as an input and returns the minimum number of brackets
you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Examples:

input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2
Constraints:

[time limit] 5000ms

[input] string text

1 ≤ text.length ≤ 5000
[output] integer

'''


from tools import timing
@timing
def bracket_match1(text):
  stack = []
  for bracket in text:
    if stack == []:
      stack.append(bracket)
    else:
      if [stack[-1], bracket] == ['(', ')']:
        stack.pop()
      else:
        stack.append(bracket)
  return len(stack)

@timing
def bracket_match(text):
  cnt = 0

  ans = 0

  for bracket in text:
    if bracket == '(':
      cnt += 1
    elif bracket == ')':
      cnt -= 1

    if cnt < 0:
      cnt += 1
      ans += 1

  return ans + cnt

text = ')'
assert bracket_match1(text) == 1
assert bracket_match(text) == 1
text = "()()()()()"
assert bracket_match1(text) == 0
assert bracket_match(text) == 0
text = "())("
assert bracket_match1(text) == 2
assert bracket_match(text) == 2
