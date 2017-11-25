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

print(selectionSort([4, 2, 1, 3]))
print(selectionSort([4, 3, 2, 1, 0, -1, -99]))
