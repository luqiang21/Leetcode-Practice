"""Selection Sort

Find the smallest card. Swap it with the first card.

Find the second-smallest card. Swap it with the second card.

Find the third-smallest card. Swap it with the third card.

Repeat finding the next-smallest card, and swapping it into the correct
position until the array is sorted.

This algorithm is called selection sort because it repeatedly selects the
next-smallest element and swaps it into place.

"""


def indexOfMinimum(array, startIndex):
    '''find the minimum index of subarray array[startIndex:]'''
    minValue = array[startIndex]
    minIndex = startIndex

    for i in range(minIndex + 1, len(array)):
        if array[i] < minValue:
            minIndex = i
            minValue = array[i]
    return minIndex


def selectionSort(array):
    '''selection sort'''
    print('original array is', array)
    for i in range(len(array)):
        minIndex = indexOfMinimum(array, i)
        if i != minIndex:
            array[i], array[minIndex] = array[minIndex], array[i]
    return array


print("Selection sort")
print(selectionSort([4, 2, 1, 3]))
print(selectionSort([4, 3, 2, 1, 0, -1, -99]))

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


def insertionSort(array):
    """insertioin sort"""
    print("original array is", array)
    # Write this method
    for i in range(0, len(array)-1):
        insert(array, i, array[i+1])

    return array


print(insertionSort([4, 2, 1, 3]))
print(insertionSort([4, 3, 2, 1, 0, -1, -99]))
