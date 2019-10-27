//Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
//
//Note:
//
//The solution set must not contain duplicate triplets.
//
//Example:
//
//Given array nums = [-1, 0, 1, 2, -1, -4],
//
//A solution set is:
//[
//  [-1, 0, 1],
//  [-1, -1, 2]
//]
//
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class MyComparison {
	public:
	bool operator() (const vector<int> lhs, const vector<int> rhs) const {
		return lhs[0] < rhs[0] || (lhs[0] == rhs[0] && lhs[1] < rhs[1]) || (lhs[0] == rhs[0] && lhs[1] == rhs[1] && lhs[2] < rhs[2]);
	}
};

class SolutionSet {
public:

    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        if (nums.size() < 3) return ans;

        for (int i = 0; i < nums.size() - 2; ++i) {
            unordered_set<int> s;
            for (int j = i + 1; j < nums.size(); ++j) {
                int x = -(nums[i] + nums[j]);
                if (s.find(x) != s.end()) {
                    vector<int> temp = {nums[i], nums[j], x};
                    sort(temp.begin(), temp.end());
                    if (find(ans.begin(), ans.end(), temp) == ans.end()) ans.push_back(temp);
                }
                else s.insert(nums[j]);
            }
        }
		sort(ans.begin(), ans.end(), MyComparison());
        return ans;
    }
};

class Solution {
public:

    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        if (nums.size() < 3) return ans;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 2; ++i) {
            if (i > 0 && nums[i] == nums[i-1]) continue;

            int l = i + 1, r = nums.size() - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    ans.push_back({nums[i], nums[l], nums[r]});
                    ++l;
                    --r;

                    while (l < r && nums[l-1] == nums[l]) ++l;
                    while (l < r && nums[r+1] == nums[r]) --r;
                }
                else if (sum < 0) {
                    ++l;
                }
                else {
                    --r;
                }
            }
        }

        return ans;
    }
};

void print(vector<vector<int>> nums) {
	for (auto rows : nums) {
		for (auto num : rows) cout << num << " " ;
		cout << endl;
	}
	cout << endl;
}
int main() {
	vector<int> nums = {-1, 0, 1, 2, -1, -4};
	print(SolutionSet().threeSum(nums));
	print(Solution().threeSum(nums));
	return 0;	
}
