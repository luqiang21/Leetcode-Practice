#include <iostream>
#include <queue>
using namespace std;

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
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return NULL;
        
        if (root -> left || root -> right) {
            TreeNode* temp = root -> left;
            root -> left = root -> right;
            root -> right = temp;
            invertTree(root -> left);
            invertTree(root -> right);
        }
        return root;
    }
};

void print(TreeNode* root) {
	if (!root) return;
	deque<pair<TreeNode*, int>> bfs;
	bfs.push_back(make_pair(root, 0));
	int lastLevel = 0;
	while (!bfs.empty()) {
		pair<TreeNode*, int> front = bfs.front();
		bfs.pop_front();
		TreeNode* node = front.first;
		if (front.second != lastLevel) cout << endl;
		cout << node -> val << "  ";
		if (node -> left) bfs.push_back(make_pair(node -> left, front.second + 1));
		if (node -> right) bfs.push_back(make_pair(node -> right, front.second + 1));
		lastLevel = front.second;
	}	
	cout << endl;
}

int main() {
	TreeNode* root = new TreeNode(4);
	root->left = new TreeNode(2);
	root->right = new TreeNode(7);
	root->left->left = new TreeNode(1);
	root->left->right = new TreeNode(3);
	root->right->left = new TreeNode(6);
	root->right->right = new TreeNode(9);

	print(root);
	Solution().invertTree(root);
	print(root);
	delete root;
	return 0;
}

