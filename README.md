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

Worst-case performance	О(n^2) comparisons, О(n) swaps
Best-case performance	О(n^2) comparisons, О(n) swaps
Average performance	О(n^2) comparisons, О(n) swaps
Worst-case space complexity	О(n) total, O(1) auxiliary

## Insertion Sort
repeatedly inserts an element in the sorted subarray to its left.

Worst-case performance	О(n^2) comparisons, swaps
Best-case performance	O(n) comparisons, O(1) swaps
Average performance	О(n^2) comparisons, swaps
Worst-case space complexity	О(n) total, O(1) auxiliary

## Merge sort
Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.

Worst-case performance	O(n log n)
Best-case performance	O(n log n) typical, O(n) natural variant
Average performance	O(n log n)
Worst-case space complexity	О(n) total, O(n) auxiliary
