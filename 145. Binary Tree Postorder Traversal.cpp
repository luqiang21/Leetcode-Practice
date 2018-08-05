#include <iostream>
#include <stack>
#include <vector>
#include <list>

using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        list<int> result;
        stack<TreeNode*> sta;

        TreeNode* p = root;
        while (!sta.empty() || p != NULL) {
            if (p != NULL) {
                sta.push(p);
                result.push_front(p -> val);
                p = p -> right;
            }
            else {
                TreeNode* node = sta.top();
                sta.pop();
                p = node -> left;
            }
        }
        vector<int> result_v{begin(result), end(result)};
        return result_v;
    }
};

class Solution1 {
public:
    void postorderTraversal(TreeNode* root, vector<int> &ans) {
        if (root == NULL) return;

        if (root -> left) {
            postorderTraversal(root -> left, ans);
        }

        if (root -> right) {
            postorderTraversal(root -> right, ans);
        }

        ans.push_back(root -> val);

    }
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        postorderTraversal(root, ans);
        return ans;
    }
};

int main() {
    TreeNode* root = new TreeNode(2);
    root -> left = new TreeNode(3);
    root -> right = new TreeNode(4);
    root -> left -> left = new TreeNode(6);
    root -> left -> right = new TreeNode(5);
    root -> right -> right = new TreeNode(7);

    Solution sol;
    std::vector<int> result = sol.postorderTraversal(root);
    for(auto i: result) cout << i << "  " ;
    cout << endl;

    Solution1 sol1;
    result = sol1.postorderTraversal(root);
    for(auto i: result) cout << i << "  ";
    cout << endl;

    return 0;
}
