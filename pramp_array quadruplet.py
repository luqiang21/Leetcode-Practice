

from tools import timing

@timing
def find_array_quadruplet(arr, s):
  n = len(arr)
  if n < 4:
    return []

  arr.sort()

  for i in range(n-3):
    for j in range(i+1, n-2):
      r = s - (arr[i] + arr[j])

      low = j + 1
      high = n - 1

      while low < high:
        if arr[low] + arr[high] < r:
          low += 1
        elif arr[low] + arr[high] > r:
          high -= 1
        else:
          return [arr[i], arr[j], arr[low], arr[high]]

  return []
arr = [1,2,3,4,5,9,19,12,12,19]
k = 40
print(arr, 'k=',k)
print(find_array_quadruplet(arr, k))

print()
arr = [2,7,4,0,9,5,1,3]
k = 20
print(arr, 'k=',k)

print(find_array_quadruplet(arr, k))
