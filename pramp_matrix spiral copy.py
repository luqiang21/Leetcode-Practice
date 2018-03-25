"""

Matrix Spiral Copy
Given a 2D array (matrix) inputMatrix of integers, create a function spiralCopy
that copies inputMatrix’s values into a 1D array in a spiral order, clockwise.
Your function then should return that array. Analyze the time and space complexities of your solution.

Example:

input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
See the illustration below to understand better what a clockwise spiral order looks like.

alt Clockwise spiral order

Constraints:

[time limit] 5000ms

[input] array.array.integer inputMatrix

1 ≤ inputMatrix[0].length ≤ 100
1 ≤ inputMatrix.length ≤ 100
[output] array.integer

"""
from tools import timing

@timing
def spiral_copy(inputMatrix):
  n = len(inputMatrix)
  m = len(inputMatrix[0])

  result = []

  top_row = 0
  bot_row = n - 1
  left_col = 0
  right_col = m - 1

  while top_row <= bot_row and left_col <= right_col:
    # copy the next top row
    for j in range(left_col, right_col+1):
      result.append(inputMatrix[top_row][j])
    top_row += 1

    # copy the next right hand side column
    for i in range(top_row, bot_row+1):
      result.append(inputMatrix[i][right_col])
    right_col -= 1

    # copy the next bottom row from right to left
    if top_row <= bot_row:
      for j in range(right_col, left_col-1, -1):
        result.append(inputMatrix[bot_row][j])
      bot_row -= 1

    # copy the next left hand side column from bottom to top
    if left_col <= right_col:
      for i in range(bot_row, top_row-1, -1):
        result.append(inputMatrix[i][left_col])
      left_col += 1
  return result

matrix = [[1]]
ans = [1]
assert spiral_copy(matrix) == ans

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
ans = [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]
assert spiral_copy(matrix) == ans
