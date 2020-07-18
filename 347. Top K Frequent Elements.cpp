class Solution {
    static bool cmp (pair<int, int>& a, pair<int, int>& b) {
        return a.second > b.second;
    }
public:
    vector<int> topKFrequentMine(vector<int>& nums, int k) {
        unordered_map<int, int> memo;
        for (auto& n : nums) {
            memo[n]++;
        }
        
        vector<pair<int, int>> vec;
        for (auto& p : memo) {
            vec.push_back(p);
        }
        
        sort(vec.begin(), vec.end(), cmp);
        vector<int> res;
        for (int i = 0; i < k; ++i) res.push_back(vec[i].first);
        
        return res;
    }
    
    
    // heap
    vector<int> topKFrequentHeap(vector<int>& nums, int k) {
        unordered_map<int, int> memo;
        for (auto& n : nums) {
            memo[n]++;
        }
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (auto& p : memo) {
            pq.push({p.second, p.first});
            if (pq.size() > k) pq.pop();
        }
        
        vector<int> res;
        while (pq.size()) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        
        return res;
    }
    
    
    // Quick select
    vector<int> topKFrequent(vector<int>& nums, int k) {
        for (auto& n : nums) {
            memo[n]++;
        }
        
        for (auto& p : memo) unique.push_back(p.first);
        
        int n = unique.size();
        quickSelect(0, n - 1, n - k);
        return vector<int>(unique.begin() + n - k, unique.end());
    }
    
private:
    unordered_map<int, int> memo;
    vector<int> unique;
    int partition(int left, int right) {
        int pivotFreq = memo[unique[right]];
        
        int storeIndex = left;
        for (int i = left; i < right; ++i) {
            if (memo[unique[i]] < pivotFreq) swap(unique[storeIndex++], unique[i]);
        }
        
        swap(unique[storeIndex], unique[right]);
        
        return storeIndex;
    }
    
    void quickSelect(int left, int right, int kSmallest) {
        if (left == right) return;
        
        int pivot = partition(left, right);
        if (pivot == kSmallest) {
            return;
        }
        else if (pivot < kSmallest) {
            quickSelect(pivot + 1, right, kSmallest);
        }
        else {
            quickSelect(left, pivot - 1, kSmallest);
        }
    }
};
