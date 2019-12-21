#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        vector<vector<bool>> board(8, vector<bool>(8, false));
        for (auto queen : queens) {
            board[queen[0]][queen[1]] = true;
        }
        
        vector<vector<int>> res;
        // 8 directions
        // up
        for (int i = king[0]; i >= 0; --i) {
            if (board[i][king[1]]) {
                res.push_back({i, king[1]});
                break;
            }
        }
        
        // up right
        int row = king[0] - 1, col = king[1] + 1;
        while (row >= 0 && col < 8) {
            if (board[row][col]) {
                res.push_back({row, col});
                break;
            }
            --row;
            ++col;
        }
        
        // right
        row = king[0];
        col = king[1] + 1;
        while (col < 8) {
            if (board[row][col]) {
                res.push_back({row, col});
                break;
            }
            ++col;
        }
        
        // right down
        row = king[0] + 1;
        col = king[1] + 1;
        while (col < 8 && row < 8) {
            if (board[row][col]) {
                res.push_back({row, col});
                break;
            }
            ++row;
            ++col;
        }
        
        // down
        row = king[0] + 1;
        col = king[1];
        while (row < 8) {
            if (board[row][col]) {
                res.push_back({row, col});
                break;
            }
            ++row;
        }
        
        // down left
        row = king[0] + 1;
        col = king[1] - 1;
        while (col >= 0 && row < 8) {
            if (board[row][col]) {
                res.push_back({row, col});
                break;
            }
            ++row;
            --col;
        }
        
        // left
        row = king[0];
        col = king[1] - 1;
        while (col >= 0) {
            if (board[row][col]) {
                res.push_back({row, col});
                break;
            }
            --col;
        }
        
        // left up
        row = king[0] - 1;
        col = king[1] - 1;
        while (col >= 0 && row >= 0) {
            if (board[row][col]) {
                res.push_back({row, col});
                break;
            }
            --row;
            --col;
        }
        
        return res;
    }
};

struct VectorHash {
    size_t operator()(const std::vector<int>& v) const {
        size_t seed = 0;
        
        seed += v[0] * 10;
        seed += v[1];
        return seed;
    }
};
class SolutionBetter {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        vector<vector<int>> res;

        unordered_set<vector<int>, VectorHash> queensSet(queens.begin(), queens.end());
        for (auto i = -1; i < 2; ++i) {
            for (auto j = -1; j < 2; ++j) {
                for (auto k = 1; k < 8; ++k) {
                    int row = king[0] + k*i, col = king[1] + k*j;
                    if (queensSet.find({row, col}) != queensSet.end()) {
                        res.push_back({row, col});
                        break;
                    }
                }
            }
        }
        
        return res;
    }
};

int main() {
	vector<vector<int>> queens = {{0, 1}, {1, 0}, {4, 0}, {0, 4}, {3, 3}, {2, 4}};
	vector<int> king = {0, 0};
	vector<vector<int>> ans = {{0, 1}, {3, 3}, {1, 0}};
	
	assert(Solution().queensAttacktheKing(queens, king) == ans);
	ans = {{0, 1}, {1, 0}, {3, 3}};
	assert(SolutionBetter().queensAttacktheKing(queens, king) == ans);
	cout << "Test passed!" << endl;
	return 0;
}
