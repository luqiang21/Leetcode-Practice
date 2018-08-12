/**
 * Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
 *
 * Each person may dislike some other people, and they should not go into the same group.
 *
 * Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
 *
 * Return true if and only if it is possible to split everyone into two groups in this way.
 *
 *
 *
 *  Example 1:
 *
 *  Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
 *  Output: true
 *  Explanation: group1 [1,4], group2 [2,3]
 *  Example 2:
 *
 *  Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
 *  Output: false
 *  Example 3:
 *
 *  Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
 *  Output: false
 *
 *
 *   Note:
 *
 *   1 <= N <= 2000
 *   0 <= dislikes.length <= 10000
 *   1 <= dislikes[i][j] <= N
 *   dislikes[i][0] < dislikes[i][1]
 *   There does not exist i != j for which dislikes[i] == dislikes[j].
 */
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    unordered_map<int, vector<int>> graph;
    unordered_map<int, bool> color;
    bool dfs(int node, bool c) {
        if (color.find(node) != color.end()) {
            return color[node] == c;
        }

        color[node] = c;

        for (auto nei: graph[node]) {
            if (!dfs(nei, c ^ 1)) {
                return false;
            }
        }

        return true;
    }
public:
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        for (auto dislike : dislikes) {
            graph[dislike[0]].push_back(dislike[1]);
            graph[dislike[1]].push_back(dislike[0]);
        }

        for (int node = 1; node < N + 1; ++node) {
            if (color.find(node) == color.end() && !dfs(node, 0)) {
                return false;
            }
        }

        return true;
    }

	void empty() {
		graph.clear();
		color.clear();
	}
};

int main() {

	Solution sol;
	int N = 4;
   	vector<vector<int>> dislikes = {{1,2},{1,3},{2,4}};
	cout << sol.possibleBipartition(N, dislikes) << endl;
	N = 3;
   	dislikes = {{1,2},{1,3},{2,3}};
	sol.empty();
	cout << sol.possibleBipartition(N, dislikes) << endl;
	return 0;
}
