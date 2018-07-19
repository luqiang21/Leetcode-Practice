#include <iostream>
#include <assert.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int height(TreeNode* root) {
        if(root == NULL) return 0;

        int l_h = height(root -> left);
        int r_h = height(root -> right);

        return max(l_h, r_h) + 1;
    }
    bool isBalanced(TreeNode* root) {
        if(root == NULL) return true;

        if(abs(height(root -> left) - height(root -> right)) > 1)
            return false;

        if(isBalanced(root -> left) && isBalanced(root -> right))
            return true;

        return false;
    }

};

int main() {
    // how to create a pointer to new TreeNode????
    TreeNode root = TreeNode(3);
    TreeNode n9 = TreeNode(9);
    TreeNode n20 = TreeNode(20);
    TreeNode n15 = TreeNode(15);
    TreeNode n7 = TreeNode(7);
    root.left = &n9;
    root.right = &n20;
    n20.left = &n15;
    n20.right = &n7;

    Solution sol;
    assert(sol.isBalanced(&root));

    cout << "test passed" << endl;
}
