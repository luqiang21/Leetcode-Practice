class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, i, j, 0, visited)) return true;
                }
            }
        }
        
        return false;
    }
    
private:
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int index, vector<vector<bool>>& visited) {
        if (index == word.length()) return true;
        if (!isValid(i, j, board) || index > word.length() || board[i][j] != word[index] || visited[i][j]) return false;
        
        visited[i][j] = true;
        vector<vector<int>> dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        for (auto& dir : dirs) {
            if (dfs(board, word, i+dir[0], j+dir[1], index + 1, visited)) return true;
        }
        visited[i][j] = false;
        return false;
    }
    
    bool isValid(int i, int j, vector<vector<char>>& board) {
        return i >= 0 && i < board.size() && j >= 0 && j < board[0].size();
    }
};
