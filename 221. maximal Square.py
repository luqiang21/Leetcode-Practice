"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

"""
from tools import timing
@timing
def maximalSquare1(matrix):
    # brute force
    if len(matrix) == 0:
        return 0
    n = len(matrix)
    m = len(matrix[0])

    max_sqlen = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                current_sqlen = 1
                flag = True
                while i + current_sqlen < n and j + current_sqlen < m and flag:
                    for k in range(j, j+current_sqlen+1):
                        if matrix[i+current_sqlen][k] == '0':
                            flag = False
                            break

                    for k in range(i, i+current_sqlen+1):
                        if matrix[k][j+current_sqlen] == '0':
                            flag = False
                            break
                    if flag:
                        current_sqlen += 1


                if max_sqlen < current_sqlen:
                    max_sqlen = current_sqlen

    return max_sqlen**2
@timing
def maximalSquare2(matrix):
    # dynamic programming
    if len(matrix) == 0:
        return 0
    n = len(matrix)
    m = len(matrix[0])

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    maxlen = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                maxlen = max(maxlen, dp[i][j])

    return maxlen**2
@timing
def maximalSquare(matrix):
    # better dynamic programming
    if len(matrix) == 0:
        return 0
    n = len(matrix)
    m = len(matrix[0])

    last_row = [0]*(m+1)

    maxlen = 0
    current_row = [0]*(m+1)
    for i in range(1, n+1):
        current_row[0] = 0
        for j in range(1, m+1):
            if matrix[i-1][j-1] == '1':
                current_row[j] = min(last_row[j], last_row[j-1], current_row[j-1]) + 1
                maxlen = max(maxlen, current_row[j])
        last_row = current_row
    return maxlen**2
matrix = [["1","0","1","1","1"],
         ["1","0","1","1","1"],
         ["1","1","1","1","1"],
         ["1","0","0","1","0"],
         ["1","0","0","1","0"]]
ans = 9
assert maximalSquare1(matrix) == ans
assert maximalSquare2(matrix) == ans
assert maximalSquare(matrix) == ans
