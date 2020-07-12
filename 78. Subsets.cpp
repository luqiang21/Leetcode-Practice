class Solution {
public:
    // bitmask
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i = pow(2, n); i < pow(2, n+1); ++i) {
            auto mask = bitset<32>(i);
            vector<int> temp;
            // bit set index is backward
            for (int j = 0; j < n; ++j) {
                if (mask.test(j)) temp.push_back(nums[j]);
            }
            res.push_back(temp);
        }
        
        return res;
    }
    
    // backtracking N * 2^N
    vector<vector<int>> subsetsBT(vector<int>& nums) {
        vector<vector<int>> res;
        int n = nums.size();
        for (int k = 0; k < nums.size() + 1; ++k) {
            backtrack(res, nums, k, 0, {});
        }
        
        return res;
    }
    
    void backtrack(vector<vector<int>>& res, vector<int>& nums, int k, int start, vector<int> cur) {
        if (cur.size() == k) res.push_back(cur);
        
        for (int i = start; i < nums.size(); ++i) {
            cur.push_back(nums[i]);
            backtrack(res, nums, k, i+1, cur);
            cur.pop_back();
        }
    }
    
    // N * 2^N
    vector<vector<int>> subsetsIterative(vector<int>& nums) {
        vector<vector<int>> res;
        res.push_back({});
        
        for (auto& num : nums) {
            vector<vector<int>> newSubsets;
            int n = res.size();
            for (int i = 0; i < n; ++i) {
                res.push_back(res[i]);
                res.back().push_back(num);
            }
            
        }
        
        return res;
    }
    
    
    vector<vector<int>> subsetsMine(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int len = 0; len <= nums.size(); ++len) {
            auto temp = getSubset(nums, len);
            res.insert(res.end(), temp.begin(), temp.end());
        }
        
        return res;
    }
    
private:
    unordered_map<string, vector<vector<int>>> map;
    vector<vector<int>> getSubset(vector<int>& nums, int len, int start=0) {
        string key = to_string(start) + " " + to_string(len);
        if (map.count(key)) return map[key];
        vector<vector<int>> res;
        
        if (len == 0) res = {{}};
        else if (len == 1) {
            for (auto& n : nums) {
                res.push_back({n});
            }
        
        }
        else if (len == 2) {
            for (int i = start; i < nums.size() - 1; ++i) {
                for (int j = i + 1; j < nums.size(); ++j) {
                    res.push_back({nums[i], nums[j]});
                }
            }
        }
        else {
            for (int i = start; i < nums.size() - len + 1; ++i) {
                auto tempRes = getSubset(nums, len-1, i+1);
                
                for (int j = 0; j < tempRes.size(); ++j) {
                    vector<int> temp = {nums[i]};
                    temp.insert(temp.end(), tempRes[j].begin(), tempRes[j].end());
                    res.push_back(temp);
                }
            }
        }
        map[key] = res;
        return res;
    }
};
