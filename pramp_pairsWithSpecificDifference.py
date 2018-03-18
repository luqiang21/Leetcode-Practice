"""
Given an array arr of distinct integers and a nonnegative integer k, write a
function findPairsWithGivenDifference that returns an array of all pairs [x,y]
in arr, such that x - y = k. If no such pairs exist, return an empty array.

In your solution, try to reduce the memory usage while maintaining time efficiency.
Prove the correctness of your solution and analyze its time and space complexities.

Note: the order of the pairs in the output array should maintain the order of the
y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input]integer k

k ≥ 0
[output] array.array.integer


"""
from tools import timing

@timing
def find_pairs_with_given_difference1(arr, k):
    res = []

    for i, num1 in enumerate(arr):
        for j, num2 in enumerate(arr):
            if num2 - num1 == k:
                res.append([num2, num1])

    return res

def binary(start, end, arr, key):
    while start <= end:
        mid = (start + end) // 2
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1

@timing
def find_pairs_with_given_difference2(arr, k):
    indices = {value: index for index, value in enumerate(arr)}
    arr.sort()
    res = {}
    for i, num1 in enumerate(arr):
        idx = binary(i+1, len(arr)-1, arr, num1 + k)
        if idx != -1:
            res[indices[num1]] = [arr[idx], num1]
    return [a[1] for a in sorted(res.items())]


# using two pointers
@timing
def find_pairs_with_given_difference(arr, k):
    indices = {value: index for index, value in enumerate(arr)}
    arr.sort()
    res = {}
    first = 0
    last = 1
    while last < len(arr) and first < len(arr):
        if first != last and arr[last] - arr[first] == k:
            res[indices[arr[first]]] = [arr[last], arr[first]]
            first += 1
            last += 1
        elif arr[last] - arr[first] < k:
            last += 1
        else:
            first += 1
    return [a[1] for a in sorted(res.items())]

arr = [4,1]
k = 3
ans = [[4, 1]]
assert find_pairs_with_given_difference1(arr, k) == ans
assert find_pairs_with_given_difference2(arr, k) == ans
assert find_pairs_with_given_difference(arr, k) == ans

arr = [0,-1,-2,2,1]
k = 1
ans = [[1,0],[0,-1],[-1,-2],[2,1]]
assert find_pairs_with_given_difference1(arr, k) == ans
assert find_pairs_with_given_difference2(arr, k) == ans
arr = [0,-1,-2,2,1]
assert find_pairs_with_given_difference(arr, k) == ans, find_pairs_with_given_difference(arr, k)

arr = [1,7,5,3,32,17,12]
k = 17
ans = []
assert find_pairs_with_given_difference1(arr, k) == ans
assert find_pairs_with_given_difference2(arr, k) == ans
arr = [1,7,5,3,32,17,12]
assert find_pairs_with_given_difference(arr, k) == ans
