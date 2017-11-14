from tools import timing
'''You are given an m x n 2D image matrix (List of Lists) where each integer
represents a pixel. Flip it in-place along its horizontal axis.

Example:

Input image :
              1 1
              0 0
Modified to :
              0 0
              1 1
'''
@timing
def flip_horizontal_axis1(matrix):
    rows = len(matrix)

    for row in range(rows//2):
        matrix[row], matrix[rows-1-row] = matrix[rows-1-row], matrix[row]


@timing
def flip_horizontal_axis2(matrix):
    matrix.reverse()

m = [[1,2], [2,1]]
print(m)
flip_horizontal_axis1(m)
print(m)

flip_horizontal_axis2(m)
print(m)
