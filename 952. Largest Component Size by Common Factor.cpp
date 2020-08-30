// 952. Largest Component Size by Common Factor
/*
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
*/

// Union by each number will need O(n^2), TLE
// had to use maximum numbers, then union by factors of each number. time O(n sqrt(max)), space O(max);

class Solution {
public:
    // by each number
    int largestComponentSize1(vector<int>& A) {
        vector<int> father(A.size(), -1);
        for (int i = 0; i < A.size(); ++i) father[i] = i;
        for (int i = 0; i < A.size() - 1; ++i) {
            for (int j = i + 1; j < A.size(); ++j) {
                // if (father[A[i]] == father[A[j]]) continue;
                if (common(A[i], A[j])) union_(father, i, j);
            }
        }
        
        int res = 0;
        unordered_map<int, int> cnts;
        for (const auto& f : father) {
            cnts[find(father, f)]++;
        }
        
        for (const auto& cnt : cnts) {
            if (cnt.second > res) res = cnt.second;
        }
        
        return res;
    }
    
    // by factors
    int largestComponentSize(vector<int>& A) {
        int maxNum = *max_element(A.begin(), A.end());
        vector<int> father(maxNum + 1);
        
        for (int i = 0; i < maxNum + 1; ++i) father[i] = i;
        for (int i = 0; i < A.size(); ++i) {
            for (int j = 2; j <= sqrt(A[i]); ++j) {
                if (A[i]%j == 0) {
                    union_(father, A[i], j);
                    union_(father, A[i], A[i] / j); // important
                }
            }
        }
        
        int res = 0;
        unordered_map<int, int> cnts;
        for (const auto& n : A) {
            res = max(res, ++cnts[find(father, n)]);
        }
        
        return res;
    }
private:
    // bool common(int n1, int n2) {
    //     int gcd = getGcd(n1, n2);
    //     return gcd > 1;
    // }
    
    // int getGcd(int n1, int n2) {
    //     while (n2 > 0) {
    //         int temp = n2;
    //         n2 = n1%n2;
    //         n1 = temp;
    //     }
    //     return n1;
    // }
    
    void union_(vector<int>& father, int n1, int n2) {
        if (father[n1] == -1 || father[n2] == -1) return;
        
        int f1 = find(father, n1);
        int f2 = find(father, n2);
        father[f2] = f1;
    }
    
    int find (vector<int>& father, int node) {
        if (father[node] == node) return node;
            
        father[node] = find(father, father[node]);
        return father[node];
    }
};
