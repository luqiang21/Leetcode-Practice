//Given a complete binary tree, count the number of nodes.
//
//Note:
//
//Definition of a complete binary tree from Wikipedia:
//In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
//
//Example:
//
//Input: 
//    1
//   / \
//  2   3
// / \  /
//4  5 6
//
//Output: 6

#include <iostream>

using namespace std;

//
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	~TreeNode() {
		delete left;
		delete right;
	}
};

class Solution {
public:
    int countNodesBruteForce(TreeNode* root) {
        if (root == NULL) return 0;
        
        return 1 + countNodesBruteForce(root -> left) + countNodesBruteForce(root -> right);
    }
    
    int countNodesLognLogn(TreeNode* root) {
        if (root == NULL) return 0;
        
        TreeNode* left = root, * right = root;
        int h = 0;
        while (right != NULL)
        {
            left = left -> left;
            right = right -> right;
            ++h;
        }
        
        if (left == NULL) return (1 << h) - 1;
        return 1 + countNodesLognLogn(root -> left) + countNodesLognLogn(root -> right);
    }

	int height(TreeNode* root) {
        return root == NULL ? -1 : 1 + height(root -> left);
    }
    int countNodes(TreeNode* root) {
        int h = height(root);
        // if right subtree height is h - 1, means left subtree is a full tree, otherwise, right subtree is a full tree
        return h < 0 ? 0 : height(root -> right) == h - 1 ? (1 << h) + countNodes(root -> right) : (1<<(h-1)) + countNodes(root -> left);
        return h < 0 ? 0 : height(root -> right) == h - 1 ? 1 + (1 << h) - 1 + countNodes(root -> right) : 1 + (1<<(h-1)) - 1 + countNodes(root -> left); // detailedly, 1(root) + number of nodes of left/right subtree + countNodes(right/left subtree)
    }
};

int main() {
	TreeNode* root = new TreeNode(1);
	root -> left = new TreeNode(2);
	root -> right = new TreeNode(3);
	root -> left -> left = new TreeNode(4);
	root -> left -> right = new TreeNode(5);
	root -> right -> left = new TreeNode(6);

	assert(Solution().countNodesBruteForce(root) == 6);
	assert(Solution().countNodesLognLogn(root) == 6);
	assert(Solution().countNodes(root) == 6);
	cout << "All tests passed!" << endl;	
	return 0;
}
