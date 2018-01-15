"""
Calculate the dictionary word that would have the most value in Scrabble
(https://en.wikipedia.org/wiki/Scrabble). Follow the methods. First write a
function to read in dictionary.txt (DICTIONARY constant) and return a list of
word. Second write a function that receives a word and calculates its value.
Use the scores stored in LETTER_SCORES. With these two pieces in place, write
a third function that takes a list of words and returns the word with the highest
value. Look at the TESTS tab to see what your code needs to pass. Enjoy!
"""

import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    data = open(DICTIONARY).read().split()
    return data


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    # my solution:
    # value = 0
    # for letter in word:
    #     value += LETTER_SCORES[letter.upper()]
    # return value

    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    # my solution
    # if words:
    #     maximum_word = None
    #     maximum_value = 0
    #     for word in words:
    #         value = calc_word_value(word)
    #         if value > maximum_value:
    #             maximum_value = value
    #             maximum_word = word
    #     return maximum_word
    #
    # else:
    #     return None


    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)


words = load_words()


def test_load_words():
    assert len(words) == 235886
    assert words[0] == 'A'
    assert words[-1] == 'Zyzzogeton'
    assert ' ' not in ''.join(words)


def test_calc_word_value():
    assert calc_word_value('bob') == 7
    assert calc_word_value('JuliaN') == 13
    assert calc_word_value('PyBites') == 14
    assert calc_word_value('benzalphenylhydrazone') == 56


def test_max_word_value():
    test_words = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
    assert max_word_value(test_words) == 'barbeque'
    assert max_word_value(words[20000:21000]) == 'benzalphenylhydrazone'
