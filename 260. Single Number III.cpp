class Solution {
public:
    vector<int> singleNumberSet(vector<int>& nums) {
        unordered_set<int> visited;
        vector<int> res;
        for (const int& n : nums) {
            if (visited.count(n)) visited.erase(n);
            else visited.insert(n);
        }
        
        for (const int& n : visited) res.push_back(n);
        
        return res;
    }
    
    
    vector<int> singleNumber(vector<int>& nums) {
        int xr = 0, num1 = 0, num2 = 0;
        for (const int& n : nums) xr ^= n; // cancel all double numbers
        
        // find first bit
        int setBit = 1;
        for (int i = 0; i < 32; ++i) {
            if (xr & setBit) break;
            setBit <<= 1;
        }
        
        for (const int& n : nums) {
            if (n & setBit) num1 ^= n;
            else num2 ^= n;
        }
        
        return {num1, num2};
    }
};
