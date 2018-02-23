'''
Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands
that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in
binaryMatrix is considered adjacent to another cell if they are next to each
either on the same row or column. Note that two values of 1 are not part of the
same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and
space complexities.

Example:

input:  binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

output: 6 # since this is the number of islands in binaryMatrix.
          # See all 6 islands color-coded below.
alt

Constraints:

[time limit] 5000ms

[input] array.array.int binaryMatrix

1 ≤ binaryMatrix.length ≤ 100
1 ≤ binaryMatrix[i].length ≤ 100
[output] integer


'''
from tools import timing
@timing
def get_number_of_islands(binaryMatrix):
    islands = 0
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])

    for i in range(rows):
        for j in range(cols):
            if binaryMatrix[i][j] == 1:
                markIsland(binaryMatrix, rows, cols, i, j)
                islands += 1
    return islands

from queue import deque
@timing
def markIsland(binaryMatrix, rows, cols, i, j):
    print('on element:', i, j,)
    q = deque()
    q.append([i,j])
    while q:
        item = q.popleft()
        x = item[0]
        y = item[1]
        if binaryMatrix[x][y] == 1:
            binaryMatrix[x][y] = -1
            pushIfValid(q, rows, cols, x-1, y)
            pushIfValid(q, rows, cols, x, y-1)
            pushIfValid(q, rows, cols, x+1, y)
            pushIfValid(q, rows, cols, x, y+1)


def pushIfValid(q, rows, cols, x, y):
    if x >= 0 and y >= 0 and x < rows and y < cols:
        q.append([x, y])

m = [[0,1,0,1,0],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0],[1,0,1,0,1]]
from pprint import pprint
pprint(m)
print('number of island:',get_number_of_islands(m))
