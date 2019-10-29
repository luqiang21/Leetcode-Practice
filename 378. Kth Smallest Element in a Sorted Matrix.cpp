#include <iostream>
#include <queue>
#include <vector>

using namespace std;

template <bool isMinHeap = false>
class MyComparison {
    public:
    bool operator() (const vector<int>& lhs, const vector<int>& rhs) const {
        if (isMinHeap) return lhs.at(0) > rhs.at(0);
        else return lhs.at(0) < rhs.at(0);
    }
};

class SolutionMaxHeapN2logK {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        // needs a max heap
        priority_queue<int> maxHeap;
        
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                if (maxHeap.size() < k)
                {
                    maxHeap.push(matrix[r][c]);
                }
                else if (maxHeap.size() == k && matrix[r][c] < maxHeap.top())
                {
                    maxHeap.pop();
                    maxHeap.push(matrix[r][c]);
                }
            }
        }
        
        return maxHeap.top();
    }
};

class SolutionKlogN {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        priority_queue<vector<int>, vector<vector<int>>, MyComparison<true>> minHeap;

        // O(n)
        for (int col = 0; col < n; ++col) minHeap.push({matrix[0][col], 0, col});

        // k - 1 times, O(k log n)
        for (int i = 0; i < k - 1; ++i) {
            vector<int> top = minHeap.top();
            int row = top.at(1), col = top.at(2);
            minHeap.pop();
            if (row < n - 1) minHeap.push({matrix[row + 1][col], row + 1, col});
        }

        return minHeap.top().at(0);
    }
};

// using upper_bound n logn log(max - min)
class SolutionUpperBound {
    public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int left = matrix[0][0], right = matrix.back().back();
        
        while (left < right) {
            int mid = left + (right - left) / 2;  // using this instead of (left + right) / 2 to prevent overflow
            int cnt = 0;
            
            for (int i = 0; i < matrix.size(); ++i) {
                cnt += upper_bound(matrix[i].begin(), matrix[i].end(), mid) - matrix[i].begin();
            }
            
            if (cnt < k) left = mid + 1;
            else right = mid;
        }
        
        return left;
    }
};

// n log(max - min)
class Solution {
    public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int left = matrix[0][0], right = matrix.back().back();
        while (left < right) {
            int mid = left + (right - left) / 2, cnt;
            cnt = search_less_equal(matrix, mid);
            
            if (cnt < k) left = mid + 1;
            else right = mid;
        }
        return left;
    }
    
    int search_less_equal(vector<vector<int>>& matrix, int target) {
        int n = matrix.size(), i = n - 1, j = 0, cnt = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] <= target) {
                cnt += i + 1;
                ++j;
            }
            else --i;
        }
        return cnt;
    }
};

int main() {
//	matrix = [
//   [ 1,  5,  9],
//   [10, 11, 13],
//   [12, 13, 15]
//],
//k = 8,
	vector<vector<int>> matrix = {{1, 5, 9},
								  {10, 11, 13},
								  {12, 13, 15}};
	int k = 8;
	assert(SolutionMaxHeapN2logK().kthSmallest(matrix, k) == 13);
	assert(SolutionKlogN().kthSmallest(matrix, k) == 13);
	assert(SolutionUpperBound().kthSmallest(matrix, k) == 13);
	assert(Solution().kthSmallest(matrix, k) == 13);
	
	cout << "Tests passed. " << endl;	

	return 0;
}

