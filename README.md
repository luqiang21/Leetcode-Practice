# Leetcode-Practice
practice makes perfect

I'll list some pseudo codes here.

## Binary Search
Below is the pseudocode for binary search, modified for searching in an array. The inputs are the array, which we call array; the number n of elements in array; and target, the number being searched for. The output is the index in array of target:

1. Let min = 0 and max=n−1.
2. If max < min, then stop; target is not present in array. Return -1.
3. Compute guess as the average of max and min, rounded down so that it is an integer.
4. If array[guess] equals target, then stop. You found it! Return guess.
5. If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
6. Otherwise, the guess was too high. Set max = guess - 1.
7. Go back to step two.

## Selection sort
sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.

## Insertion Sort
repeatedly inserts an element in the sorted subarray to its left.
