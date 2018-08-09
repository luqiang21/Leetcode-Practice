/*
 * Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
 *
 * Note:
 * Each of the array element will not exceed 100.
 * The array size will not exceed 200.
 * Example 1:
 *
 * Input: [1, 5, 11, 5]
 *
 * Output: true
 *
 * Explanation: The array can be partitioned as [1, 5, 5] and [11].
 * Example 2:
 *
 * Input: [1, 2, 3, 5]
 *
 * Output: false
 *
 * Explanation: The array cannot be partitioned into equal sum subsets.
 */

#include <iostream>
#include <unordered_set>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
	public:
		    unordered_set<string> memo;
		        bool dfs(vector<int>& nums, int start, int target) {
				        if (target <= 0) return target == 0;
					        
					        if (memo.find(to_string(start) + "-" + to_string(target)) != memo.end()) return false;
						        
						        for (int i = start; i < nums.size(); ++i) {
								            if (dfs(nums, i+1, target - nums[i])) return true;
									            }
							        memo.insert(to_string(start) + "-" + to_string(target));
								        return false;
									    }
			    bool canPartition(vector<int>& nums) {
				            int sum = accumulate(nums.begin(), nums.end(), 0);
					            sort(nums.begin(), nums.end());
						            return !(sum&1) && dfs(nums, 0, sum >> 1);
							        }
};

int main() {

	Solution sol;
	vector<int> nums = {1, 5, 11, 5};
	cout << sol.canPartition(nums) << endl;
	return 0;
}
