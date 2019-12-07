#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        if (heightMap.empty()) return 0;
        
        int m = heightMap.size(), n = heightMap[0].size(), res = 0, mx = INT_MIN;
        priority_queue< pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > q;
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        vector<vector<int>> dir{{0, -1}, {-1, 0}, {1, 0}, {0, 1}};
        
        // boundaries
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                    q.push({heightMap[i][j], i * n + j});
                    visited[i][j] = true;
                }
            }
        }

        
        while (!q.empty()) {
            auto t = q.top(); q.pop();
            int h = t.first, r = t.second / n, c = t.second % n;
            mx = max(h, mx);
            
            for (int i = 0; i < 4; ++i) {
                int x = r + dir[i][0], y = c + dir[i][1];
                if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y]) continue;
                
                if (heightMap[x][y] < mx) res += mx - heightMap[x][y];
                q.push({heightMap[x][y], x * n + y});
                visited[x][y] = true;
            }
        }
        
        return res;
    }
};


int main() {
	vector<vector<int>> heightMap = {{1, 4, 3, 1, 3, 2},
									 {3, 2, 1, 3, 2, 4},
									 {2, 3, 3, 2, 3, 1}};
	cout << Solution().trapRainWater(heightMap) << endl;

	return 0;
}
