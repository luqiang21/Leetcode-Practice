/**
Find a duplicate, Space Edition™.

We have a vector of integers, where:

The integers are in the range 1..n1..n
The vector has a length of n+1n+1
It follows that our vector has at least one integer which appears at least twice.
But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our vector.
(If there are multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip Macbook Pro With Retina Display™.
Thing is, the damn thing came with the RAM soldered right to the motherboard,
so we can't upgrade our RAM. So we need to optimize for space!
*/

/**
Our approach is similar to a binary search, except we divide the range of possible
answers in half at each step, rather than dividing the vector in half.

1. Find the number of integers in our input vector which lie within the range
1..n/2 .
2. Compare that to the number of possible unique integers in the same range.
3. If the number of actual integers is greater than the number of possible integers,
we know there’s a duplicate in the range 1..n/2​ , so we iteratively use the same
approach on that range.
4. If the number of actual integers is not greater than the number of possible
integers, we know there must be duplicate in the range n/2 + 1..n, so we
iteratively use the same approach on that range.
5. At some point our range will contain just 1 integer, which will be our answer.
*/

#include <iostream>
#include <vector>

using namespace std;

unsigned int findRepeat(const vector<unsigned int>* theVector) {
  unsigned int floor = 1;
  unsigned int ceiling = theVector.size() - 1;

  while(floor < ceiling) {
    // divide range
    unsigned int midpoint = floor + ((ceiling - floor) / 2);
    unsigned int lowerFloor = floor;
    unsigned int lowerCeiling = midpoint;
    unsigned int upperFloor = midpoint + 1;
    unsigned int upperCeiling = ceiling;

    // count number of items in lower range
    unsigned int itermsInLowerRange = 0;
    for(unsigned int item: theVector) {
      if(item >= lowerFloor && item <= lowerCeiling) {
        ++ itermsInLowerRange;
      }
    }

    unsigned int distinctPossibleIntsInLower = lowerCeiling - lowerFloor + 1;

    if(itermsInLowerRange > distinctPossibleIntsInLower) {
      floor = lowerFloor;
      ceiling = lowerCeiling;
    }
    else {
      floor = upperFloor;
      ceiling = upperCeiling;
    }
  }
  // floor and ceiling have converged
  // we found a number that repeats
  return floor;
}
