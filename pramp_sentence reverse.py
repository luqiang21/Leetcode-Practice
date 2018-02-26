'''
Sentence Reverse
You are given an array of characters arr that consists of sequences of characters
separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array
in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
Constraints:

[time limit] 5000ms

[input] array.character arr

0 ≤ arr.length ≤ 100
[output] array.character


'''


from tools import timing

@timing
def reverse_words1(arr):
  # use a stack, time O(N), space O(N)
  i = len(arr) - 1
  res = []
  word = []
  for i in range(len(arr)):
    if arr[i] != ' ':
      word.append(arr[i])
    else:
      if word != []:
        res.append(word)
      word = []
      res.append(arr[i])
  if word != []:
        res.append(word)
  arr = []
  # print(res)
  for j in range(len(res)):
    if res[-1] == " ":
      arr.append(res.pop())
    else:
      arr += res.pop()
  return arr

@timing
def reverse_words(arr):
  # reverse all chars
  n = len(arr)
  mirror_reverse(arr, 0, n-1)

  # reverse each word:
  word_start = None
  for i in range(n):
    if arr[i] == ' ':
      if word_start != None:
        mirror_reverse(arr, word_start, i-1)
        word_start = None
    elif i == n-1:
      # last word
      if word_start != None:
        mirror_reverse(arr, word_start, i)
    else:
      if word_start == None:
        word_start = i
  return arr

def mirror_reverse(arr, start, end):
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

arr = ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"]
print(arr)
print(reverse_words1(arr))
print()
print(arr)
print(reverse_words(arr))
