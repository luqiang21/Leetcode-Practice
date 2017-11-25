# Leetcode-Practice
practice makes perfect

I'll list some pseudo codes here.

## Binary Search
Below is the pseudocode for binary search, modified for searching in an array. The inputs are the array, which we call array; the number n of elements in array; and target, the number being searched for. The output is the index in array of target:

Let min = 0 and max=n−1.
Compute guess as the average of max and min, rounded down so that it is an integer.
If array[guess] equals target, then stop. You found it! Return guess.
If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
Otherwise, the guess was too high. Set max = guess - 1.
Go back to step two.
