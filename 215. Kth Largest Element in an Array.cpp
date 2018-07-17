#include <iostream>
#include <vector>
#include <queue>
#include "assert.h"

using namespace std;

class Solution {
public:
    /**
    * @brief find the kth largest number in an array
    * @param nums the array of integers
    * @param k given k
    * @return the kth largest number
    */
    int findKthLargest2(vector<int>& nums, int k) {
        priority_queue<int> pq(nums.begin(), nums.end());
        for (int i = 1; i < k; ++i ){
            pq.pop();
        }

        return pq.top();
    }
};

int main() {
    Solution sol;
    vector<int> nums{3,2,3,1,2,4,5,5,6};
    int k = 4;

    assert(sol.findKthLargest2(nums, k) == 4);
    cout << "test passed" << endl;
}
