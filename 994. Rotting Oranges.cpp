class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        queue<pair<int, int>> q;
        int fresh = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                }
                if (grid[i][j] == 1) fresh++;

            }
        }
        if (fresh == 0) return 0;
        int cnt = 0;
        
        vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        while (!q.empty()) {
            ++cnt;
            int size = q.size();
            for (int idx = 0; idx < size; ++idx) {
                auto pair = q.front();
                q.pop();
                int row = pair.first, col = pair.second;
                for (auto& dir : dirs) {
                    int newRow = dir.first + row, newCol = dir.second + col;
                    if (isValid(newRow, newCol, grid) && grid[newRow][newCol] == 1) {
                        grid[newRow][newCol] = 2;
                        q.push({newRow, newCol});
                        --fresh;
                    }
                }
            }
        }
        
        
        if (fresh == 0) return cnt - 1;
        return -1;
    }
    
private:
    bool isValid(int r, int c, vector<vector<int>>& grid) {
        return r >= 0 && r < grid.size() && c >= 0 && c < grid[0].size();
    }
        
};



