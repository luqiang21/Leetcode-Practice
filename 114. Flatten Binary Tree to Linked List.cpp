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
    void flatten1(TreeNode* root) {
        traverse(root);
    }
    
private:
    TreeNode* pre = nullptr;
    void traverse(TreeNode* root) {
        if (root == nullptr) return;
        
        traverse(root -> right);
        traverse(root -> left);
        
        root -> right = pre;
        root -> left = nullptr;
        pre = root;
    }
    
public:
    void flatten2(TreeNode* root) {
        flattenTree(root);
    }
    
private:
    TreeNode* flattenTree(TreeNode* node) {
        if (node == nullptr) return node;
        
        if (!node -> left && !node -> right) return node;
        
        auto leftTail = flattenTree(node -> left);
        auto rightTail = flattenTree(node -> right);
        
        if (leftTail) {
            leftTail -> right = node -> right;
            node -> right = node -> left;
            node -> left = nullptr;
        }
        
        if (rightTail) return rightTail;
        return leftTail;
    }
   
public:
    void flatten(TreeNode* root) {
        if (!root) return;
        
        auto node = root;
        while (node) {
            if (node -> left) {
                auto rightMost = node -> left;
                while (rightMost -> right) rightMost = rightMost -> right;
                
                rightMost -> right = node -> right;
                node -> right = node -> left;
                node -> left = nullptr;
            }
            node = node -> right;
        }
    }
};
