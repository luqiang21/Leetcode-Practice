'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
 rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
from tools import timing
class Solution(object):
    @timing
    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        if numRows == 1 or numRows >= len(s):
            return s
        """
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)

    # more concise and compact version
    @timing
    def convert2(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        step = (numRows == 1) - 1 # 0 or -1
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows - 1:
                step = -step # change direction
            idx += step
        return ''.join(rows)

    # My own thought, pattern exists for all elements.
    # every 2 * numRows - 2 is a same pattern, solved by reference to @tju_xu97
    '''
    For example, the following has 4 periods(cycles):

    P   | A   | H   | N
    A P | L S | I I | G
    Y   | I   | R   |
    The size of every period is defined as "cycle"

    cycle = (2*nRows - 2), except nRows == 1.
    In this example, (2*nRows - 2) = 4.

    In every period, every row only has two elements, except the first
    row and the last row which have only one element.

    Suppose the current row is i, the index of the first element is j:

    j = i + cycle*k, k = 0, 1, 2, ...
    The index of the second element is secondJ:

    secondJ = (j - i) + cycle - i
    (j-i) is the start of current period, (j-i) + cycle is the start of next period.
    '''
    @timing
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        cycle, length, res = 2 * numRows - 2, len(s), ""
        for i in xrange(numRows):
            for j in xrange(i, length, cycle):
                res += s[j]
                secondJ = (j - i) + cycle - i

                # if not the first row or last row and within length:
                if secondJ < length and i not in [0, numRows - 1]:
                    res += s[secondJ]
        return res

s = "PAYPALISHIRING"
print Solution().convert1(s, 3) #"PAHNAPLSIIGYIR"

print Solution().convert2(s, 3) #"PAHNAPLSIIGYIR"

print Solution().convert(s, 3) #"PAHNAPLSIIGYIR"
