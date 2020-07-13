/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTreeRec(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL) return true;
        if (p != NULL && q != NULL) 
            return p -> val == q -> val && isSameTree(p -> left, q -> left)
                && isSameTree(p -> right, q -> right);
        return false;
    }
    
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<pair<TreeNode*, TreeNode*>> queue;
        queue.push_back({p, q});
        
        while (queue.size()) {
            auto cur = queue.back();
            queue.pop_back();
            auto curP = cur.first, curQ = cur.second;
            if (curP == NULL && curQ == NULL) continue;
            if ((curP == NULL || curQ == NULL) || curP -> val != curQ -> val) return false;
            
            queue.push_back({curP -> left, curQ -> left});
            queue.push_back({curP -> right, curQ -> right});
        }
        
        return true;
    }
};
