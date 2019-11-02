#include <iostream>
#include <queue>
using namespace std;
//Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
//
//For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
//
//    1
//   / \
//  2   2
// / \ / \
//3  4 4  3
//
//
//But the following [1,2,2,null,3,null,3] is not:
//
//    1
//   / \
//  2   2
//   \   \
//   3    3
//
//
//Note:
//Bonus points if you could solve it both recursively and iteratively.

//**
// * Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class SolutionRecursive {
public:
    bool isSymmetric(TreeNode* left, TreeNode* right) {
        if (left == NULL && right == NULL) return true;
        if (left == NULL || right == NULL) return false;

        if (left -> val == right -> val) return isSymmetric(left -> left, right -> right) && isSymmetric(left -> right, right -> left);
        return false;
    }

    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;

        return isSymmetric(root -> left, root -> right);
    }
};

class SolutionIterative1 {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        
        deque<TreeNode*> queue;
        queue.push_back(root -> left);
        queue.push_back(root -> right);
        
        while (!queue.empty()) {
            TreeNode* curLeft = queue.front();
            queue.pop_front();
            TreeNode* curRight = queue.front();
            queue.pop_front();
            
            if (curLeft == NULL && curRight == NULL) continue;
            if (curLeft == NULL || curRight == NULL || curLeft -> val != curRight -> val) return false;
            
            queue.push_back(curLeft -> left);
            queue.push_back(curRight -> right);
            queue.push_back(curLeft -> right);
            queue.push_back(curRight -> left);
        }
        
        return true;
    }
};

class Solution {
public:
    bool isPalindrome(vector<TreeNode*> level) {
        if (level.size() <= 1) return true;

        int n = level.size();
        for (int i = 0; i < n/2; ++i) {
            if (level.at(i) == NULL && level.at(n - 1 - i) == NULL) continue;
            if (level.at(i) == NULL || level.at(n - 1 - i) == NULL) return false;

            if (level.at(i) -> val != level.at(n - 1 - i) -> val) return false;
        }
        return true;
    }
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;

        vector<TreeNode*> previousLevel;
        previousLevel.push_back(root);

        while (!previousLevel.empty()) {
            vector<TreeNode*> curLevel;

            for (TreeNode* node : previousLevel) {
                if (node != NULL) {
                    curLevel.push_back(node -> left);
                    curLevel.push_back(node -> right);
                }
            }

                if (!isPalindrome(curLevel)) return false;
                previousLevel = curLevel;

        }

        return true;
    }
};

int main() {
	TreeNode* root1 = new TreeNode(1);
	root1 -> left = new TreeNode(2);
	root1 -> right = new TreeNode(2);
	root1 -> left -> left = new TreeNode(3);
	root1 -> left -> right = new TreeNode(4);
	root1 -> right -> left = new TreeNode(4);
	root1 -> right -> right = new TreeNode(3);

	TreeNode* root2 = new TreeNode(1);
	root2 -> left = new TreeNode(2);
	root2 -> right = new TreeNode(2);
	root2 -> left -> right = new TreeNode(3);
	root2 -> right -> right = new TreeNode(3);

	assert(SolutionRecursive().isSymmetric(root1) == true);
	assert(SolutionRecursive().isSymmetric(root2) == false);
	assert(SolutionIterative1().isSymmetric(root1) == true);
	assert(SolutionIterative1().isSymmetric(root2) == false);
	assert(Solution().isSymmetric(root1) == true);
	assert(Solution().isSymmetric(root2) == false);
	cout << "All tests passed!" << endl;
	return 0;
}
