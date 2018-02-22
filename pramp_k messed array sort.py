'''
Given an array of integers arr where each element is at most k places away from
its sorted position, code an efficient function sortKMessedArray that sorts arr.
For instance, for an input array of size 10 and k = 2, an element belonging to
index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in
the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer k

1 ≤ k ≤ 20
[output] array.integer

'''
from tools import timing

@timing
def sort_k_messed_array1(arr, k):
  """
  Args:
    arr: list of integers
    k: the places away from its sorted position
  Returns:
    arr: sorted arr
  """
  if len(arr) == 1:
    return arr

  for i in range(len(arr)-1):
    smallest = None
    idx = None
    for j in range(i, min((i+k+1), len(arr))):
      if smallest is None or arr[j] < smallest:
        smallest = arr[j]
        idx = j
    # exchange numbers
    if idx != i:
      arr[i], arr[idx] = arr[idx], arr[i]

  return arr

@timing
def sort_k_messed_array2(arr, k):
  # insertion sort
  for i in range(1, len(arr)):
    x = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > x:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = x
  return arr

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert sort_k_messed_array1(arr, k) == ans
assert sort_k_messed_array2(arr, k) == ans


arr = [6,1,4,11,2,0,3,7,10,5,8,9]
k = 6
ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert sort_k_messed_array1(arr, k) == ans
assert sort_k_messed_array2(arr, k) == ans
