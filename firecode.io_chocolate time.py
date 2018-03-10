"""
There are N students standing in a line where each student has some points.
You distribute chocolates to these students under the following constraints:

   1. Each student must have at least one chocolate.
   2. Students with a higher point value get more chocolates than their neighbors.

Write a method distributeChocolate to compute the minimum number of chocolates
distributed such that the above conditions are satisfied.

Example:

distributeChocolate("[1,5,7,1]") ==> 7

In this example, input is a list of points which 4 different students have been
allotted. The minimum number of chocolates distributed i.e. the output is 7.
"""
from tools import timing
@timing
def distributeChocolate(points):
    if len(points) < 1:
        return 0
    chocolate = [1] * len(points)

    for i in range(1, len(points)):
        if points[i] > points[i-1]:
            chocolate[i] = chocolate[i-1] + 1

    for i in range(len(points) - 2, -1, -1):
        if points[i] > points[i+1] and chocolate[i] <= chocolate[i+1]:
            chocolate[i] = chocolate[i+1] + 1
    print("chocolate", chocolate)
    return sum(chocolate)

points = [1,5,7,1]
ans = 7
print("points", points)

assert distributeChocolate(points) == ans

print()
points = [2, 3, 3, 2, 1, 5, 2]
ans = 12
print("points", points)

assert distributeChocolate(points) == ans
