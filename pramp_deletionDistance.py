

# I didn't solve this in the interview, shame on me.


"""
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need
to delete in the two strings in order to get the same string. For instance, the
deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in
both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance
that returns the deletion distance between them. Explain how your function works,
and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer

"""
from tools import timing

@timing
def deletion_distance1(str1, str2):
  n = len(str1)
  m = len(str2)
  mem = [[0 for _ in range(m+1)] for _ in range(n+1)]

  for i in range(n+1):
    mem[i][0] = i
  for j in range(m+1):
    mem[0][j] = j

  for i in range(1, n+1):
    for j in range(1, m+1):
      if str1[i - 1] == str2[j - 1]:
        mem[i][j] = mem[i-1][j-1]
      else:
        mem[i][j] = min(mem[i][j-1], mem[i-1][j]) + 1

  return mem[n][m]

@timing
def deletion_distance(str1, str2):
  dist = 0
  if str1 == "" or str2 == "":
    return len(str1) or len(str2)

  if str1[0] == str2[0]:
    dist = deletion_distance(str1[1:], str2[1:])
  else:
    dist = min(deletion_distance(str1, str2[1:]), deletion_distance(str1[1:], str2)) + 1
  return dist

str1, str2 = "some", "thing"
ans = 9
assert deletion_distance1(str1, str2) == ans
assert deletion_distance(str1, str2) == ans
