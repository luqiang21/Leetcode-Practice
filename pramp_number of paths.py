'''
You’re testing a new driverless car that is located at the Southwest (bottom-left)
corner of an n×n grid. The car is supposed to get to the opposite, Northeast
(top-right), corner of the grid. Given n, the size of the grid’s axes, write a
function numOfPathsToDest that returns the number of the possible paths the driverless
car can take.

alt the car may move only in the white squares

For convenience, let’s represent every square in the grid as a pair (i,j). The
first coordinate in the pair denotes the east-to-west axis, and the second coordinate
denotes the south-to-north axis. The initial state of the car is (0,0), and the
destination is (n-1,n-1).

The car must abide by the following two rules: it cannot cross the diagonal border.
In other words, in every step the position (i,j) needs to maintain i >= j. See
the illustration above for n = 5. In every step, it may go one square North (up),
or one square East (right), but not both. E.g. if the car is at (3,1), it may go
to (3,2) or (4,1).

Explain the correctness of your function, and analyze its time and space complexities.

Example:

input:  n = 4

output: 5 # since there are five possibilities:
          # “EEENNN”, “EENENN”, “ENEENN”, “ENENEN”, “EENNEN”,
          # where the 'E' character stands for moving one step
          # East, and the 'N' character stands for moving one step
          # North (so, for instance, the path sequence “EEENNN”
          # stands for the following steps that the car took:
          # East, East, East, North, North, North)
Constraints:

[time limit] 5000ms

[input] integer n

1 ≤ n ≤ 100
[output] integer
'''

from tools import timing
@timing
def num_of_paths_to_dest1(n):
    '''
    Args:
        n: dimension of square grid
        i >= j
    '''
    if n <= 2:
        return 1
    # right, top
    i, j = 0, 0
    cnt = 0
    path = [[0 for _ in range(n)] for _ in range(n)]
    path[0][0] = 1
    for i in range(1, n):
        for j in range(0, n):
            if i >= j:
                if j == 0:
                    path[i][j] = path[i-1][j]
                if i == 0:
                    path[i][j] = path[i][j-1]
                else:

                    path[i][j] = path[i][j-1] + path[i-1][j]
    return path[n-1][n-1]

@timing
def num_of_paths_to_dest2(n):
    '''
    Args:
        n: dimension of square grid
        i >= j
    Returns:
        number of paths to (n-1, n
    '''
    # use recursion here
    memo = [[-1 for _ in range(n)] for _ in range(n)]
    return num_of_paths_to_square(n-1, n-1, memo)

def num_of_paths_to_square(i, j, memo):
    if i < 0 or j < 0:
        return 0
    elif i < j:
        memo[i][j] = 0
    elif memo[i][j] != -1:
        return memo[i][j]
    elif i == 0 or j == 0:
        memo[i][j] = 1
    else:
        memo[i][j] = num_of_paths_to_square(i, j-1, memo) + num_of_paths_to_square(i-1, j, memo)
    return memo[i][j]
@timing
def num_of_paths_to_dest(n):
    '''
    Args:
        n: dimension of square grid
        i >= j
    Returns:
        number of paths to (n-1, n
    '''
    # use two rows everytime. Since we only need the value from East and South, two rows are sufficient
    if n == 1:
        return 1

    last_row = [1 for _ in range(n)] # n items, first item is not used

    current_row = last_row
    for j in range(1,n):
        for i in range(j, n):
            if i == j:
                current_row[i] = last_row[i]
            else:
                current_row[i] = last_row[i] + current_row[i-1]
        last_row = current_row
    return current_row[-1]


n = 1
assert num_of_paths_to_dest1(n) == 1
assert num_of_paths_to_dest2(n) == 1
assert num_of_paths_to_dest(n) == 1

n = 2
assert num_of_paths_to_dest1(n) == 1
assert num_of_paths_to_dest2(n) == 1
assert num_of_paths_to_dest(n) == 1


n = 17
assert num_of_paths_to_dest1(n) == 35357670
assert num_of_paths_to_dest2(n) == 35357670
assert num_of_paths_to_dest(n) == 35357670
print("all tests passed.")
