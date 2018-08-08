/** Given an m x n matrix of non-negative integers representing the height of
each unit cell in a continent, the "Pacific ocean" touches the left and top
edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to
another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses
in above matrix).
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void dfs(vector<vector<int>>& matrix, int i, int j, vector<vector<bool>>& ocean_matrix, int m, int n) {
        ocean_matrix[i][j] = true;
        vector<pair<int, int>> directions;
        directions.push_back(make_pair(1, 0));
        directions.push_back(make_pair(-1, 0));
        directions.push_back(make_pair(0, 1));
        directions.push_back(make_pair(0, -1));

        for (auto pair: directions) {
            int x = i + pair.first;
            int y = j + pair.second;
            if(x < 0 || x >= m || y < 0 || y >= n || ocean_matrix[x][y] || matrix[x][y] < matrix[i][j]) {
                continue;
            }
            dfs(matrix, x, y, ocean_matrix, m, n);
        }

    }

    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (!matrix.size()) return {};

        int m = matrix.size(), n = matrix[0].size();
        vector<pair<int, int>> result;
        vector<vector<bool>> p_matrix(m, vector<bool>(n, false));
        vector<vector<bool>> a_matrix(m, vector<bool>(n, false));

        for(int i = 0; i < m; ++i) {
            dfs(matrix, i, 0, p_matrix, m, n);
            dfs(matrix, i, n-1, a_matrix, m, n);
        }

        for(int j = 0; j < n; ++j) {
            dfs(matrix, 0, j, p_matrix, m, n);
            dfs(matrix, m-1, j, a_matrix, m, n);
        }

        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                if(p_matrix[i][j] && a_matrix[i][j]) {
                    result.push_back(make_pair(i, j));
                }
            }
        }

        return result;
    }
};

int main() {
    vector< vector<int> > matrix = { {1,2,2,3,5},
                                    {3,2,3,4,4},
                                    {2,4,5,3,1},
                                    {6,7,1,4,5},
                                    {5,1,1,2,4}};
    Solution sol;
    for(auto pair : sol.pacificAtlantic(matrix)) {
        cout << pair.first << " " << pair.second << endl;
    }

    return 0;
}
