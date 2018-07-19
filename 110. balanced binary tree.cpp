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
    TreeNode* root = new TreeNode(3);
    TreeNode* n9 = new TreeNode(9);
    TreeNode* n20 = new TreeNode(20);
    TreeNode* n15 = new TreeNode(15);
    TreeNode* n7 = new TreeNode(7);
    root -> left = n9;
    root -> right = n20;
    n20 -> left = n15;
    n20 -> right = n7;

    Solution sol;
    assert(sol.isBalanced(root));

    cout << "test passed" << endl;
    delete root;
    delete n9;
    delete n20;
    delete n15;
    delete n7;
}
