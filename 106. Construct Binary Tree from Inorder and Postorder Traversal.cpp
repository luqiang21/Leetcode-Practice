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
    TreeNode* buildTree1(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.size() == 0) return NULL;
        
        TreeNode* head = new TreeNode(postorder.back());
        postorder.pop_back();
        int idx = getIndex(inorder, head -> val);

        auto it = inorder.begin() + idx;
        auto secondHalf = vector<int>(it + 1, inorder.end());
        head -> right = buildTree(secondHalf, postorder);
        auto firstHalf = vector<int>(inorder.begin(), it);
        head -> left = buildTree(firstHalf, postorder);
        
        return head;
    }
private:
    int getIndex(vector<int>& list, int key) {
        auto it = find(list.begin(), list.end(), key);
        return it - list.begin();
    }
    
public:
    // better without sub vectors
    TreeNode* buildTree2(vector<int>& inorder, vector<int>& postorder) {
        for (int i = 0; i < inorder.size(); ++i) {
            idxMap[inorder[i]] = i;
        }
        return buildTree(0, inorder.size() - 1, inorder, postorder);
    }
private:
    unordered_map<int, int> idxMap;
    
    TreeNode* buildTree(int inLeft, int inRight, vector<int>& inorder, vector<int>& postorder) {
        if (inLeft > inRight) return NULL;
        
        int val = postorder.back();
        postorder.pop_back();
        TreeNode* root = new TreeNode(val);
        
        int index = idxMap[val];
        root -> right = buildTree(index + 1, inRight, inorder, postorder);
        root -> left = buildTree(inLeft, index - 1, inorder, postorder);
        
        return root;
    }
    
    
public:
    // iterative
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.size() != postorder.size() || inorder.size() == 0) return nullptr;
        for (int i = 0; i < inorder.size(); ++i) {
            idxMap[inorder[i]] = i;
        }
        
        stack<TreeNode*> stack;
        int n = inorder.size(), val = postorder[n-1];
        TreeNode* root = new TreeNode(val);
        stack.push(root);
        
        for (int i = n - 2; i >= 0; --i) {
            val = postorder[i];
            TreeNode* node = new TreeNode(val);
            
            if (!stack.empty() && idxMap[stack.top() -> val] < idxMap[val]) {
                stack.top() -> right = node;
            }
            else {
                TreeNode* parent = nullptr;
                while (!stack.empty() && idxMap[stack.top() -> val] > idxMap[val]) {
                    parent = stack.top();
                    stack.pop();
                }
                if (parent != nullptr) parent -> left = node;
            }
            
            stack.push(node);
        }
        
        return root;
    }
        
};
