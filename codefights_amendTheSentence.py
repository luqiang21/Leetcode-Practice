"""
You have been given a string s, which is supposed to be a sentence. However,
someone forgot to put spaces between the different words, and for some reason
they capitalized the first letter of every word. Return the sentence after
making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.
Example

For s = "CodefightsIsAwesome", the output should be
amendTheSentence(s) = "codefights is awesome";
For s = "Hello", the output should be
amendTheSentence(s) = "hello".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string containing uppercase and lowercase English letters.

Guaranteed constraints:

3 ≤ s.length ≤ 100.

[output] string

The amended sentence.
"""
from tools import timing

@timing
def amendTheSentence1(s):
    words = []
    word = None
    for l in s:
        if word == None:
            word = l.lower()
            continue
        if l.isupper() and word:
            words.append(word)
            word = l.lower()
        else:
            word += l
    words.append(word)
    return " ".join(words)

@timing
def amendTheSentence(s):
    s = list(s)
    for i,x in enumerate(s):
        if x.isupper():
            s[i] = x.lower()
            if i != 0:
                s[i] = ' ' + s[i]
    return ''.join(s)

s = "CodefightsIsAwesome"
print(amendTheSentence1(s))
print(amendTheSentence(s))
