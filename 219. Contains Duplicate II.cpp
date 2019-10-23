//Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
//
//Example 1:
//
//Input: nums = [1,2,3,1], k = 3
//Output: true
//Example 2:
//
//Input: nums = [1,0,1,1], k = 1
//Output: true
//Example 3:
//
//Input: nums = [1,2,3,1,2,3], k = 2
//Output: false
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> mostRecentVisited;
        for (int i = 0; i < nums.size(); ++i) {
            if (mostRecentVisited.find(nums[i]) != mostRecentVisited.end()) {
                if (i - mostRecentVisited[nums[i]] <= k) return true;
            }
                mostRecentVisited[nums[i]] = i;
        }
        return false;
    }
};

int main() {
	Solution sol;
	vector<int> nums = {1, 2, 3, 1};
	cout << std::boolalpha << sol.containsNearbyDuplicate(nums, 3) << endl;
}
