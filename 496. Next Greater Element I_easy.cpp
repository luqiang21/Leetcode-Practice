#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>

using namespace std;


class SolutionBruteForce {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans(nums1.size(), -1);
        for (int i = 0; i < nums1.size(); ++i) {
            bool found = false;
            for (int j = 0; j < nums2.size(); ++j) {
                if (found && nums2[j] > nums1[i]) {
                    ans[i] = nums2[j];
                    break;
                }
                if (nums1[i] == nums2[j]) {
                    found = true;
                }
            }
        }

        return ans;
    }
};

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans(nums1.size(), -1);

        stack<int> s; // keep a decreasing sub-sequence.
        unordered_map<int, int> map; // map from number x to its next greater number
        for (int num : nums2) {
            while (!s.empty() && s.top() < num) {
                map[s.top()] = num;
                s.pop();
            }
            s.push(num);
        }

        for (int i = 0; i < nums1.size(); ++i) {
            if (map.count(nums1[i])) ans[i] = map[nums1[i]];
        }
        return ans;
    }
};

int main() {
	//	Example 1:
	//Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
	//Output: [-1,3,-1]
	//Explanation:
	//    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
	//    For number 1 in the first array, the next greater number for it in the second array is 3.
	//    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
	//Example 2:
	//Input: nums1 = [2,4], nums2 = [1,2,3,4].
	//Output: [3,-1]
	//Explanation:
	//    For number 2 in the first array, the next greater number for it in the second array is 3.
	//    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.	
	vector<int> nums1 = {4, 1, 2}, nums2 = {1, 3, 4, 2}, ans = {-1, 3, -1};
	assert(SolutionBruteForce().nextGreaterElement(nums1, nums2) == ans);
	assert(Solution().nextGreaterElement(nums1, nums2) == ans);

	nums1 = {2, 4}, nums2 = {1, 2, 3, 4}, ans = {3, -1};
	assert(SolutionBruteForce().nextGreaterElement(nums1, nums2) == ans);
	assert(Solution().nextGreaterElement(nums1, nums2) == ans);
	cout << "Tests passed." << endl;
	return 0;
}
