
board = [[".",".",".","7",".",".","3",".","1"],
         ["3",".",".","9",".",".",".",".","."],
         [".","4",".","3","1",".","2",".","."],
         [".","6",".","4",".",".","5",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".","1",".",".","8",".","4","."],
         [".",".","6",".","2","1",".","5","."],
         [".",".",".",".",".","9",".",".","8"],
         ["8",".","5",".",".","4",".",".","."]]
from tools import timing
import math

import math
def get_candidates(board, row, col):
    # For some empty cell board[row][col], what possible
    # characters can be placed into this cell
    # that aren't already placed in the same row,
    # column, and sub-board?
    # At the beginning, we don't have any candidates
    candidates = []

    # For each character add it to the candidate list
    # only if there's no collision, i.e. that character
    # doesn't already exist in the same row, column
    # and sub-board. Notice the top-left corner of (row, col)'s
    # sub-board is (row - row%3, col - col%3).
    chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in chars:
        collision = False
        for i in range(9):
            if board[row][i] == char or board[i][col] == char or board[(row-row%3) + int(math.floor(i/3))][(col-col%3) + i%3]==char:
                collision = True
                break
        if not collision:
             candidates.append(char)
    return candidates

def sudoku_solve(board):
    # For each empty cell, consider 'newCandidates', the
    # set of possible candidate values that can
    # be placed into that cell.
    row = -1
    col = -1
    candidates = None

    # find out where to start
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                newCandidates = get_candidates(board, r, c)
                # Then, we want to keep the smallest
                # sized 'newCandidates', plus remember the
                # position where it was found
                if candidates == None or len(newCandidates) < len(candidates):
                    candidates = newCandidates
                    row = r
                    col = c

        # If we have not found any empty cell, then
    # the whole board is filled already
    if candidates == None:
        return True

    # For each possible value that can be placed
    # in position (row, col), let's
    # place that value and then recursively query
    # whether the board can be solved.  If it can,
    # we are done.
    for val in candidates:
        board[row][col] = val
        if sudoku_solve(board):
           return True

        # The tried value val didn't work so restore
        # the (row, col) cell back to '.'
        board[row][col] = '.'

    # Otherwise, there is no value that can be placed
    # into position (row, col) to make the
    # board solved
    return False



from pprint import pprint
pprint(board)
print(sudoku_solve(board))

board = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
pprint(board)
print(sudoku_solve(board))
