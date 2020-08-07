/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


class Solution {
public:
    vector<vector<int>> verticalTraversalMine(TreeNode* root) {
        vector<vector<int>> res;
        if (root == nullptr) return res;
        
        vector<vector<int>> positions;
        queue<pair<TreeNode*, int>> q;
        
        q.push({root, 0});
        positions.push_back({0, 0, root -> val});
        
        while (!q.empty()) {
            auto node = q.front();
            q.pop();
            auto pos = positions[node.second];
            auto cur = node.first;
            
            if (cur -> left) {
                q.push({cur -> left, positions.size()});
                positions.push_back({pos[0] - 1, pos[1] + 1, cur -> left -> val});
            }
            
            if (cur -> right) {
                q.push({cur -> right, positions.size()});
                positions.push_back({pos[0] + 1, pos[1] + 1, cur -> right -> val});
            }
        }
        
        
        sort(positions.begin(), positions.end());//, compare);
        res.push_back({positions[0][2]});
        for (int i = 1; i < positions.size(); ++i) {
            if (positions[i][0] == positions[i-1][0]) res.back().push_back(positions[i][2]);
            else res.push_back({positions[i][2]});
        }
        
        return res;
    }
private:
    // useful if we -1 for y
    static bool compare(const vector<int>& v1, const vector<int>& v2) {
        return v1[0] < v2[0] || (v1[0] == v2[0] && v1[1] > v2[1])
            || (v1[0] == v2[0] && v1[1] == v2[1] && v1[2] < v2[2]);
    }
    
    
    
public:
    vector<vector<int>> verticalTraversalIterative(TreeNode* root) {
        vector<vector<int>> res;
        if (root == nullptr) return res;
        
        map<int, map<int, multiset<int>>> nodes;
        // queue<pair<TreeNode*, pair<int, int>>> todo; // for bfs
        stack<pair<TreeNode*, pair<int, int>>> todo;

        todo.push({root, {0, 0}});
        
        while (!todo.empty()) {
            // auto p = todo.front(); // for bfs
            auto p = todo.top();
            
            todo.pop();
            auto node = p.first;
            auto x = p.second.first, y = p.second.second;
            nodes[x][y].insert(node -> val);
            
            if (node -> left) todo.push({node -> left, {x - 1, y + 1}});
            if (node -> right) todo.push({node -> right, {x + 1, y + 1}});
        }
        
        for (auto p : nodes) {
            vector<int> col;
            for (auto q : p.second) {
                col.insert(col.end(), q.second.begin(), q.second.end());
            }
            res.push_back(col);
        }
        
        return res;
    }
    
    
    vector<vector<int>> verticalTraversalRec(TreeNode* root) {
        vector<vector<int>> res;
        if (root == nullptr) return res;
        
        map<int, map<int, multiset<int>>> nodes;
        
        dfs(root, 0, 0, nodes);
        
        for (auto p : nodes) {
            vector<int> col;
            for (auto q : p.second) {
                col.insert(col.end(), q.second.begin(), q.second.end());
            }
            res.push_back(col);
        }
        
        return res;
    }
private:
    void dfs(TreeNode* root, int x, int y, map<int, map<int, multiset<int>>>& nodes) {
        nodes[x][y].insert(root -> val);
        if (root -> left) dfs(root -> left, x - 1, y + 1, nodes);
        if (root -> right) dfs(root -> right, x + 1, y + 1, nodes);
    }
};
