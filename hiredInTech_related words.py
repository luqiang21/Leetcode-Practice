'''
Task: Related words
A company analysing news articles needs to identify relations between words in
these articles. One simple idea that its engineers have is to look at pairs of
words that are often seen close to each other.

You goal will be to help this company in its experiment. Write a program, which
given a text T and a word W, finds the word, which is most often seen around word W.

We define “seen around word W” as a word, which is within the N words before and
after an occurrence of the word W.

For example if we have the text “It is a nice day today, the sun is shining.”
and our word W is “day” and N=3, then the words around W are “is”, “a”, “nice”,
“today”, “the” and “sun”. These are the words that come immediately before or
after “day” within the distance of 3.

The goal is for all occurrences of W in T to consider the words that are around
these occurrences and to return the one that is most often seen. If there are
more than one such words return the one that comes first lexicographically.

Don’t count the occurrences of the word W around other occurrences of it. Also,
don’t count the same word more than once even if it’s around more than one occurrence of W.

If the text has no occurrences of the word W, return the string “N/A” (quotes
are not part of the string).

The input is read from the standard input. The first line contains the text T.
The second line contains the word W and the third line contains the number N.

The result must be printed to the standard output. It must contain one word as
was described above.

The text T will contain words consisting of only lower-case and upper-case latin
letters and numbers. When counting words you must ignore the casing. This means
that “today” and “Today” is the same word. When printing the result use lower-case.
The text T will also contain other symbols like ‘,’, ‘.’, ‘!’, ‘?’, but not only.
You must strip out everything that is not a letter or a digit. Such symbols should
not be counted as part of the words.

Here is an example:

SAMPLE INPUT

It is a nice day today, the sun is shining. However, the weather is expected to
get worse the following few days. Nice day by day weather forecasts can be found
literally everywhere on the “Internet”. So, it is quite easy to know what to
expect tomorrow.

day

3

SAMPLE OUTPUT

nice

There are three occurrences of the word ‘day’ within the text. Note that we don’t
 count the word ‘days’ as an occurrence. Only exact word matches are considered.

Near the first occurrence are the words ‘is’, ‘a’, ‘nice’, ‘today’, ‘the’, ‘sun’.

Near the second occurrence are the words ‘few, ‘days’, ‘nice’, ‘by’, ‘day’, ‘weather’.
However, we won’t consider the word ‘day’ because it’s the same as W in the example.

Near the third occurrence are the words ‘nice’, ‘day’, ‘by’, ‘weather’, ‘forecasts’,
‘can’. However, the first four words are already covered by the second occurrence of W,
so we WILL NOT count the one more time.

In the end we have the following list of words that were found to be around
occurrences of the word ‘day’: 'is', 'a', 'nice', 'today', 'the', 'sun', 'nice',
'few', 'days', 'by', 'weather', 'forecasts', 'can'.

In this list all words are seen only once except the word ‘nice’, which is seen
twice. This is why this is the correct output for this sample input.
'''
# below is fast but hard to remember
# T = T.translate(str.maketrans("", "", string.punctuation)) # remove punctuations
def related_words(T, W, N):
    import string
    T = "".join(ch for ch in T if ch not in string.punctuation)
    cur = 0 # explored
    visited = {}
    max_ = 0
    T = T.split()
    exist = False
    T = [word.lower() for word in T]
    W = W.lower()
    for i, word in enumerate(T):
        if word == W:
            for j in range(max(i-N, cur), min(i+N+1,len(T))):
                if T[j] != W:
                    # not counting itself
                    visited[T[j]] = visited.get(T[j], 0) + 1
                    if  visited[T[j]] > max_:
                        max_ = visited[T[j]]
            cur = min(i+N, len(T)-1)
            exist = True
    if not exist:
        print("N/A")
    else:
        ''' takes O(nlogn)'''
        # res = []
        # for word, cnt in visited.items():
        #     if cnt == max_:
        #         res.append(word)
        # res.sort()
        # print(res[0])
        related_word = None
        for word, cnt in visited.items():
            if cnt == max_ and (not related_word or word < related_word):
                related_word = word
        print(related_word)
T = '''It is a nice day today, the sun is shining. However, the weather is expected to
get worse the following few days. Nice day by day weather forecasts can be found
literally everywhere on the “Internet”. So, it is quite easy to know what to expect tomorrow.'''

W = 'day'

N = 3
related_words(T, W, N)
