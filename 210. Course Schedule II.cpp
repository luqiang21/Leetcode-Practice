class Solution {
public:
    // use in degrees
    vector<int> findOrder1(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegrees(numCourses, 0);
        vector<vector<int>> adjList(numCourses, vector<int>());
        
        for (auto& pre : prerequisites) {
            indegrees[pre[0]]++;
            adjList[pre[1]].push_back(pre[0]);
        }
        
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indegrees[i] == 0) q.push(i);
        }
        
        vector<int> res;
        while (q.size() > 0) {
            auto cur = q.front();
            q.pop();
            res.push_back(cur);
            for (auto& c : adjList[cur]) {
                indegrees[c]--;
                if (indegrees[c] == 0) q.push(c);
            }
        }
        
        if (res.size() == numCourses) return res;
        return {};
    }
    
    
    // dfs
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjList(numCourses, vector<int>());
        
        for (auto& pre : prerequisites) {
            adjList[pre[1]].push_back(pre[0]);
        }
        
        vector<int> res;
        unordered_map<int, int> color;
        for (int i = 0; i < numCourses; ++i) color[i] = WHITE;
        
        for (int i = 0; i < numCourses; ++i) {
            if (color[i] == WHITE) dfs(i, res, color, adjList);
        }
        
        reverse(res.begin(), res.end());
        if (isPossible) return res;
        return {};
    }
private:
    bool isPossible = true;
    int WHITE = 1, GRAY = 2, BLACK = 3;
    
    void dfs(int course, vector<int>& res,
        unordered_map<int, int>& color,
        vector<vector<int>>& adjList) {
        if (!isPossible) return;
        
        color[course] = GRAY;
        for (auto& nei : adjList[course]) {
            if (color[nei] == WHITE) dfs(nei, res, color, adjList);
            else if (color[nei] == GRAY) isPossible = false;
        }
        
        color[course] = BLACK;
        res.push_back(course);
    }
    
};
