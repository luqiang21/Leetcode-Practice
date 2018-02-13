"""
You are given a grid of cells with size N rows by M columns. A robot is situated
at the bottom-left cell (row N-1, column 0). It can move from cell to cell but
only to the right and to the top. Some cells are empty and the robot can pass
through them but others are not and the robot cannot enter such cells. The robot
cannot go outside the grid boundaries.

The robot has a goal to reach top-right cell (row 0, column M-1). Both the start
and end cells are always empty. You need to compute the number of different paths
that the robot can take from start to end. Only count paths that visit empty cells
and move only to the right and up.

N and M will be numbers in the range [1, 512].

Write a method, which accepts the grid as an argument and returns one integer
 - the total number of different paths that the robot can take from the start to
 the end cell, MODULO 1,000,003. The reason we will use the modulo operation here
 is that the actual result could become a really big number and we don't want to let
  handling big numbers complicate the task more.

The input grid will contain N strings with M characters each - either '0' or '1',
with '0' meaning an empty cell and '1' meaning an occupied cell. Each of these
strings corresponds to a row in the grid.
"""

from tools import timing

@timing
def count_the_paths(grid):
    N = len(grid) # row
    M = len(grid[0]) # column
    return numberOfPaths(0, M-1, grid)

def numberOfPaths(n, m, grid):

    if grid[n][m] == '1':
        return 0

    elif(n == len(grid) - 1 and m == 0):
        # base case
        return 1

    elif n == len(grid) - 1:
        return numberOfPaths(n, m-1, grid)
    elif m == 0:
        return numberOfPaths(n+1, m, grid)
    else:
        return numberOfPaths(n+1, m, grid) + numberOfPaths(n, m-1, grid)


@timing
def count_the_paths1(grid):
    # Write your solution here
    N = len(grid)
    M = len(grid[0])
    F = [[0 for _ in range(M)] for _ in range(N)]

    # base
    F[N-1][0] = 1


    for x in range(N-1, -1, -1):
        for y in range(M):
            if grid[x][y] == '0':
                if x == N-1 and y == 0:
                    continue
                if x == N-1:
                    F[x][y] = F[x][y-1]
                elif y == 0:
                    F[x][y] = F[x+1][y]
                else:
                    F[x][y] = F[x][y-1] + F[x+1][y]

            # print(x, y, F[x][y])

    ans = F[0][M-1] % 1000003
    return ans

grid = ['00000', '01110', '01110', '00000']
print(count_the_paths(grid))
print(count_the_paths1(grid))
grid = ['0']
print(count_the_paths(grid))
print(count_the_paths1(grid))
grid = ['0000000', '0000000', '0000000', '0000000', '0000000']
print(count_the_paths(grid))
print(count_the_paths1(grid))
