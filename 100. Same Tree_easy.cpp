#include <iostream>
using namespace std;

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {        
        if (p == NULL || q == NULL) return p == q;
        
        return p -> val == q -> val && isSameTree(p -> left, q -> left) && isSameTree(p -> right, q -> right);
    }
};

int main() {
	TreeNode* root = new TreeNode(1);
	root->left = new TreeNode(2);
	root->right = new TreeNode(3);

	TreeNode* root1 = root;
	cout << boolalpha << Solution().isSameTree(root, root1) << endl;
	delete root;
	return 0;
}
