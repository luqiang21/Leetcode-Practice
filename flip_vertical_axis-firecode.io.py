from tools import timing

@timing
def flip_vertical_axis1(matrix):
    cols = len(matrix[0])
    for row in range(len(matrix)):
      for col in range(cols//2):
        matrix[row][col],matrix[row][cols-col-1] = matrix[row][cols-col-1],matrix[row][col]
    print matrix

@timing
def flip_vertical_axis2(matrix):
    for m in matrix:
        m.reverse()
        # m = m[::-1]

    # for i in range(len(matrix)):
        # matrix[i] = matrix[i][::-1]
        # matrix[i].reverse()
    print matrix


matrix = [[0,1], [1,2]]
print matrix

flip_vertical_axis1(matrix)
print matrix
flip_vertical_axis2(matrix)
