#include <iostream>
#include <vector>
using namespace std;

vector<int> countingSort(const vector<int>& theVector, int maxValue) {
  vector<size_t> numCounts(maxValue + 1);

  // populate numCounts
  for(int num: theVector) {
    ++ numCounts[num];
  }

  // populate the final sorted vector
  vector<int> sortedVector(theVector.size());
  size_t currentSortedIndex = 0;

  // for each num in numCounts;
  for(size_t num = 0; num < numCounts.size(); ++num) {
    size_t count = numCounts[num];

    // for the number of times the item occurs
    for(size_t i = 0; i < count; ++i) {
      // add it to the sorted array
      sortedVector[currentSortedIndex] = num;
      ++ currentSortedIndex;
    }
  }
  return sortedVector;
}

int main() {
  vector<int> theVector {3, 2, 1, 5};
  for(auto num: theVector) {
    cout << num << " ";
  }
  cout << endl;
  vector<int> ans = countingSort(theVector, 5);
  for(auto num: ans) {
    cout << num << " ";
  }
  cout << endl;
}
