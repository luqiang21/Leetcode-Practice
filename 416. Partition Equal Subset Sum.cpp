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
	bool canPartitionMemo(vector<int>& nums) {
	    int sum = accumulate(nums.begin(), nums.end(), 0);
	    sort(nums.begin(), nums.end());
	    return !(sum&1) && dfs(nums, 0, sum >> 1);
	}

	
    bool canPartitionKnap(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum%2 != 0) return false;
        
        vector<bool> dp(sum/2 + 1, false);
        dp[0] = true;
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = sum/2; j > 0; --j) {
                if (nums[i] <= j) {
                    dp[j] = dp[j] || dp[j-nums[i]];
                }
            }
        }
        return dp.back();
    }
    
    bool canPartitionRecur(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum%2 != 0) return false;
        sort(nums.rbegin(), nums.rend());
        return dfs(nums, sum/2, 0);
    }
    
    bool dfs(vector<int>& nums, int target, int i) {
        if (i >= nums.size() || nums[i] > target) return false;
        if (nums[i] == target) return true;
        return dfs(nums, target-nums[i], i + 1) || dfs(nums, target, i + 1);
    }
    
	// bitset
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum%2 != 0) return false;
        bitset<10001> bits(1);
        for (auto num : nums) bits |= bits << num;
        return bits[sum/2];
    }
};

int main() {

	Solution sol;
	vector<int> nums = {1, 5, 11, 5};
	cout << sol.canPartition(nums) << endl;
	return 0;
}
