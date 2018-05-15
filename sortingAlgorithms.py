"""Selection Sort

Find the smallest card. Swap it with the first card.

Find the second-smallest card. Swap it with the second card.

Find the third-smallest card. Swap it with the third card.

Repeat finding the next-smallest card, and swapping it into the correct
position until the array is sorted.

This algorithm is called selection sort because it repeatedly selects the
next-smallest element and swaps it into place.

"""
from tools import timing

def index_of_minimum(array, startIndex):
    '''find the minimum index of subarray array[startIndex:]'''
    minValue = array[startIndex]
    minIndex = startIndex

    for i in range(minIndex + 1, len(array)):
        if array[i] < minValue:
            minIndex = i
            minValue = array[i]
    return minIndex


def selection_sort(array):
    '''selection sort'''
    print('original array is', array)
    for i in range(len(array)):
        minIndex = index_of_minimum(array, i)
        if i != minIndex:
            array[i], array[minIndex] = array[minIndex], array[i]
    return array


print("Selection sort")
print(selection_sort([4, 2, 1, 3]))
print(selection_sort([4, 3, 2, 1, 0, -1, -99]))

"""
Insertion sort

Insertion sort repeatedly inserts an element in the sorted
subarray to its left.

Call insert to insert the element that starts at index 1 into the sorted
    subarray in index 0.
Call insert to insert the element that starts at index 2 into the sorted
    subarray in indices 0 through 1.
Call insert to insert the element that starts at index 3 into the sorted
    subarray in indices 0 through 2.
Finally, call insert to insert the element that starts at index n-1 into
    the sorted subarray in indices 0 through n−2.
"""


def insert(array, rightIndex, value):
    """ insert helper function"""
    j = rightIndex
    while j >= 0 and array[j] > value:
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = value


def insertion_sort(array):
    """insertioin sort"""
    print("original array is", array)
    # Write this method
    for i in range(0, len(array)-1):
        insert(array, i, array[i+1])

    return array


print("Insertion sort.")
print(insertion_sort([4, 2, 1, 3]))
print(insertion_sort([4, 3, 2, 1, 0, -1, -99]))


"""
Merge sort
"""
# Takes in an array that has two sorted subarrays,
#  from [p..q] and [q+1..r], and merges the array


def merge(array, p, q, r):
    """ merge """
    print("merge called", p, q, r, '\n', array)
    lh = q - p + 1
    rh = r - q

    L = [0] * (lh)
    R = [0] * (rh)

    for i in range(0, lh):
        L[i] = array[p + i]
    for j in range(0, rh):
        R[j] = array[q + 1 + j]

    i, j, k = 0, 0, p

    while i < lh and j < rh:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # either L or R is exhausted, above while loop exits.
    while i < lh:
        array[k] = L[i]
        i += 1
        k += 1

    while j < rh:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort(array, p, r):
    """ Takes in an array and recursively merge sorts it"""
    if p < r:
        print("merge_sort called", p, r, '\n', array)
        q = (p+r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)

@timing
def merge_sort2(arrayList):
    """ Not using helper function, more clear """
    if len(arrayList) > 1:
        mid = len(arrayList) // 2
        leftHalf = arrayList[:mid]
        rightHalf = arrayList[mid:]

        merge_sort2(leftHalf)
        merge_sort2(rightHalf)

        i, j, k = 0, 0, 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                arrayList[k] = leftHalf[i]
                i += 1
            else:
                arrayList[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            arrayList[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arrayList[k] = rightHalf[j]
            j += 1
            k += 1
@timing
def merge_sort3(arrayList):
    """ Not using helper function, more clear """
    if len(arrayList) > 1:
        mid = len(arrayList) // 2
        leftHalf = arrayList[:mid]
        rightHalf = arrayList[mid:]

        merge_sort3(leftHalf)
        merge_sort3(rightHalf)

        i, j, k = 0, 0, 0
        while i < len(leftHalf) and j < len(rightHalf):
            is_left_done = i >= len(leftHalf)
            is_right_done = j >= len(rightHalf)

            if (not is_left_done) and (is_right_done or leftHalf[i] <= rightHalf[j]):
                arrayList[k] = leftHalf[i]
                i += 1
            else:
                arrayList[k] = rightHalf[j]
                j += 1
            k += 1



print("Merge Sort.")
array = [6, 3, 8, 2, 7, 1]
print('before sorting,', array)
merge_sort(array, 0, len(array)-1)
print('after sorting,', array)


array = [4, 2, 1, 3]
print('before sorting,', array)
merge_sort(array, 0, len(array)-1)
print('after sorting,', array)


array = [6, 3, 8, 2, 7, 1]
print('before sorting,', array)
merge_sort2(array)
print('after sorting,', array)


array = [4, 2, 1, 3]
print('before sorting,', array)
merge_sort2(array)
print('after sorting,', array)

rray = [6, 3, 8, 2, 7, 1]
print('before sorting,', array)
merge_sort3(array)
print('after sorting,', array)


array = [4, 2, 1, 3]
print('before sorting,', array)
merge_sort3(array)
print('after sorting,', array)

"""
Quick sort
"""


def partition(array, low, high):
    """ partition """
    # select the last element as pivot
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quick_sort(array, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now
        # at right place
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


print()
array1 = [6, 3, 8, 2, 7, 1]
print('before sorting,', array1)
quick_sort(array1, 0, len(array1)-1)
print('after sorting,', array1)


array2 = [4, 2, 1, 3]
print('before sorting,', array2)
quick_sort(array2, 0, len(array2)-1)
print('after sorting,', array2)

""" Heap Sort"""
# copy from geeksforgeeks
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

# Driver code to test above
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print('array is', arr)
print ("Sorted array is", arr)
