'''
Write a divide and conquer version of merge sort that sorts the list in place,
i.e. without creating any additional lists or slices of the input list.
refer: http://penguin.ewu.edu/cscd300/Topic/AdvSorting/MergeSorts/InPlace.html
'''
def mergeSortInPlace(A,low,high):
    print('divide', A, low, high)
    if low >= high-1:
        return
    else:
        mid = (low + high) // 2
        mergeSortInPlace(A,low,mid)
        mergeSortInPlace(A,mid,high)

    left = low
    right = mid
    if A[mid-1] <= A[right]:
        return
    while left < mid and right < high:
        if A[left] <= A[right]:
            left +=1
        else:
            tmp = A[right]
            A[left+1:right+1]=A[left:right]
            A[left] = tmp
            left +=1
            mid +=1
            right +=1
    print('merge', A, low, high)

A = [3,2,1,4,3]
mergeSortInPlace(A, 0, len(A))
assert A == [1,2,3,3,4]

B = [3,4,2,1,7,5,8,9,0,6]
# mergeSortInPlace(B, 0, len(B))
print("test passed.")
