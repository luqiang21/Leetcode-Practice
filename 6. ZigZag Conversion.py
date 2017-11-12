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
    def convert(self, s, numRows):
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



s = "PAYPALISHIRING"
print Solution().convert1(s, 3) #"PAHNAPLSIIGYIR"

print Solution().convert(s, 3) #"PAHNAPLSIIGYIR"
