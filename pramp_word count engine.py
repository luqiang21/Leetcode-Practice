"""
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string
document and returns a list of all unique words in it and their number of occurrences,
sorted by the number of occurrences in a descending order. If two or more words
have the same count, they should be sorted according to their order in the original
sentence. Assume that all letters are in english alphabet. You function should
be case-insensitive, so for instance, the words “Perfect” and “perfect” should
be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use
whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for
time while keeping a polynomial space complexity.

Examples:

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"],
          ["get", "1"], ["by", "1"], ["just", "1"] ]
Important: please convert the occurrence integers in the output list to strings
(e.g. "3" instead of 3). We ask this because in compiled languages such as C#,
Java, C++, C etc., it’s not straightforward to create mixed-type arrays
(as it is, for instance, in scripted languages like JavaScript, Python, Ruby etc.).
The expected output will simply be an array of string arrays.

Constraints:

[time limit] 5000ms
[input] string document
[output] array.array.string

"""

from tools import timing
from collections import OrderedDict

@timing
def word_count_engine(document):
  # clean
  words_dic = OrderedDict()
  words = document.lower().split()
  largest = 0
  for i, word in enumerate(words):
    word_list = []
    for letter in word:

      if letter.isalpha():
        word_list.append(letter)
    if len(word_list) == 0:
      continue

    words[i] = "".join(word_list)
    if words[i] not in words_dic.keys():
      words_dic[words[i]] = 1
    else:
      words_dic[words[i]] += 1
    if words_dic[words[i]] > largest:
      largest = words_dic[words[i]]
  # output
  res = [None]*(largest + 1)

  for word, count in words_dic.items():
    word_counter_list = res[count]
    if word_counter_list is None:
      word_counter_list = []
    word_counter_list.append(word)
    res[count] = word_counter_list

  output = []
  for i in range(len(res)-1, -1, -1):
    if res[i] is not None:
      for j in range(len(res[i])):
        output.append([res[i][j], str(i)])

  return output
document = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
ans =  [['just', '4'], ['practice', '3'], ['perfect', '2'], ['makes', '1'], ['youll', '1'], ['get', '1'], ['by', '1']]
assert word_count_engine(document) == ans
