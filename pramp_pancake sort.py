'''
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are
allowed to use only the function flip you wrote in the first step in order to
make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.

Note: it’s called pancake sort because it resembles sorting pancakes on a plate
with a spatula, where you can only use the spatula to flip some of the top pancakes
in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.

Constraints:

[time limit] 5000ms

[input] array.integer arr

[input] integer k

0 ≤ k
[output] array.integer


'''
import math
from tools import timing
def flip(arr, k):
  mid = int(math.floor(k / 2))
  for i in range(mid+1):
    arr[i], arr[k-i] = arr[k-i], arr[i]

# mine solution, took unnecessary steps of flip
@timing
def pancake_sort1(arr):
  n = len(arr)
  for j in range(n-1, 0, -1):
    for i in range(1, j+1):
      if arr[0] < arr[i]:
        flip(arr,i)

    flip(arr, j)
  return arr

@timing
def pancake_sort(arr):
  n = len(arr)
  for j in range(n-1, 0, -1):
    max_index = findMaxIndexInPrefix(arr, j)
    flip(arr, max_index)

    flip(arr, j)

  return arr

def findMaxIndexInPrefix(arr, k):
  ans = 0
  for i in range(k+1):
    if arr[i] > arr[ans]:
      ans = i
  return ans

arr = [1, 5, 4, 3, 2]
print(pancake_sort1(arr))
arr = [1, 5, 4, 3, 2]
print(pancake_sort(arr))
