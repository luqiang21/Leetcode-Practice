#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        vector<vector<string>> ans;
        backtrack(0, board, ans);
        return ans;
    }
    
    void backtrack(int row, vector<string>& board, vector<vector<string>>& ans) {
        if (row == board.size()) ans.push_back(board);
        else {
            for (int col = 0; col < board.size(); ++col) {
                if (!isValid(row, col, board)) continue;
                
                board[row][col] = 'Q';
                backtrack(row + 1, board, ans);
                board[row][col] = '.';
            }
        }
    }
    
    bool isValid(int row, int col, vector<string>& board) {
        // check upper
        for (int i = 0; i < row; ++i) {
            if (board[i][col] == 'Q') return false;
        }
        
        // check left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; --i, --j) {
            if (board[i][j] == 'Q') return false;
        }
        
        // check right diagonal
            for (int i = row - 1, j = col + 1; i >= 0 && j < board.size(); --i, ++j) {
            if (board[i][j] == 'Q') return false;
        }
        return true;
    }
};

int main() {

	auto ans = Solution().solveNQueens(4);
	for (auto strList : ans) {
		for (auto str : strList) {
			cout << str << endl;
		}
		cout << endl;
	}
	return 0;
}
