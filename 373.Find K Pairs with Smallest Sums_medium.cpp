#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class MyComparison1 {
    public:
    bool operator() (const pair<int, int>& lhs, const pair<int, int>& rhs) {
        return lhs.first + lhs.second < rhs.first + rhs.second;
    }
};
class Solution_n2logn {
public:

    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> allPairs;
        for (int i = 0; i < nums1.size(); ++i) {
            for (int j = 0; j < nums2.size(); ++j) {
                allPairs.push_back(make_pair(nums1[i], nums2[j]));
            }
        }
        sort(allPairs.begin(), allPairs.end(), MyComparison1());
        vector< vector<int> > ans;
        for (int i = 0; i < min(k, (int)allPairs.size()); ++i) {
            ans.push_back({allPairs[i].first, allPairs[i].second});
        }
        
        return ans;
        
    }
};

template<bool min_queue = false>
class MyComparison {
    public:
    bool operator() (const vector<int>& lhs, const vector<int>& rhs) const {
		if (!min_queue) return lhs[0] + lhs[1] < rhs[0] + rhs[1];
		return lhs[0] + lhs[1] > rhs[0] + rhs[1];
    }
};

class Solution_n2logk {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue<vector<int>, vector< vector<int> >, MyComparison<>> max_heap;
        for (int i = 0; i < nums1.size(); ++i) {
            for (int j = 0; j < nums2.size(); ++j) {
                if (max_heap.size() < k) max_heap.push({nums1[i], nums2[j]});
                else {
                    vector<int> pair = max_heap.top();
                    int sum = pair[0] + pair[1];
                    if (sum > (nums1[i] + nums2[j])) {
                        max_heap.pop();
                        max_heap.push({nums1[i], nums2[j]});
                    }
                }
            }
        }
        
        vector<vector<int>> ans(max_heap.size());
		k = max_heap.size() - 1;
        while (!max_heap.empty()) {
            ans[k--] = max_heap.top();
            max_heap.pop();
        }
        
        return ans;
    }
};


class Solution_klogk {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<vector<int>> ans;
        if (nums1.size() == 0 || nums2.size() == 0 || k == 0) return ans;
        
        priority_queue<vector<int>, vector<vector<int>>, MyComparison<true>> min_hp;
        for (int i = 0; i < nums1.size(); ++i) min_hp.push({nums1[i], nums2[0], 0}); // last number is index for number in nums2
        
        while (k > 0 && !min_hp.empty()) {
            vector<int> top = min_hp.top();
            min_hp.pop();
            ans.push_back({top[0], top[1]});
            k --;
            
            if (top[2] + 1 < nums2.size()) min_hp.push({top[0], nums2[top[2] + 1], top[2] + 1});
        }
        return ans;
    }
};

void print(vector<vector<int>> nums) {
	for (auto num : nums) {
		cout << num[0] << ", " << num[1] << "   "; 
	}
	cout << endl;
}
int main() {
//Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
//Output: [[1,2],[1,4],[1,6]] 
//Explanation: The first 3 pairs are returned from the sequence: 
//             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
	vector<int> nums1 = {1, 7, 11}, nums2 = {2, 4, 6};
	int k = 3;
	vector<vector<int>> ans = {{1, 2}, {1, 4}, {1, 6}};
	
	print(Solution_n2logn().kSmallestPairs(nums1, nums2, k));
	print(Solution_n2logk().kSmallestPairs(nums1, nums2, k));
	print(Solution_klogk().kSmallestPairs(nums1, nums2, k));
	
	return 0;
}
