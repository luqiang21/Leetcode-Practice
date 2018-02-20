'''
You are given a text T consisting of words in which there may be typos. Your task
 is to count how many times a given word W is used in this text. However, you need
 to include in this count the cases in which this word was written with a typo.

It's hard to say if a word contains a typo or not, especially if you don't have
a good dictionary. For this task, a word W' in T is considered to be an instance
of W if:

it's exactly the same as W
it has the same length as W and up to 2 letters are different
W' can be obtained from W by removing or adding 1 letter

For example if W = banana the following words are instances of it with typos:

bamama (2 letters are changed)
bananas (one added letter)
banna (one letter was missed out)
The length of W will be in the range [5, 20]. The input text T will be no longer
than 10,000 symbols. It will contain only lower case latin letters and spaces
used to separate the words.

Input is read from the standard input. On the first line will be the word W.
On the second line will be the text to search.

The result is written to the standard output. It must consist of one integer - the
number of occurrences of W in the text including the typos as defined above.

SAMPLE INPUT

banana
there are three bananas on the tree and one banano on the ground
SAMPLE OUTPUT

2
'''

T = 'there are three bananas on the tree and one banano on the ground'
W = 'banana'
T = T.split()
m = len(W)

cnt = 0
for word in T:
    # compare word with W to determine typo or not
    if word == W:
        cnt += 1
        continue

    # check it has the same length as W and up to 2 letters are different
    if len(word) == m:
        # whether up to 2 letters are different
        diff = 0
        for ch1, ch2 in zip(word, W):
            if ch1 != ch2:
                diff += 1
            if diff > 2:
                break
        if diff <= 2:
            cnt += 1
    # elif len(word) - m == 1:

    #   W' can be obtained from W by removing or adding 1 letter
    elif abs(len(W) - len(word)) == 1:
        i = j = 0
        longer = W if len(W) > len(word) else word
        shorter = W if len(W) < len(word) else word
        misses = 0
        while i < len(shorter) and j < len(longer):
            if shorter[i] != longer[j]:
                j += 1
                misses += 1
            else:
                i += 1
                j += 1
            if j - i > 1:
                break
        if misses <= 1:
            cnt += 1
print('T is',T)
print('W is', W)
print('The number of typos:', cnt)
