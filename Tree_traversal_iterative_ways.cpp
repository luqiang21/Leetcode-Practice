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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> sta;

        TreeNode* p = root;
        while (!sta.empty() || p != NULL) {
            if (p != NULL) {
                sta.push(p);
                result.push_back(p -> val);
                p = p -> left;
            }
            else {
                TreeNode* node = sta.top();
                sta.pop();
                p = node -> right;
            }
        }

        return result;
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> sta;

        TreeNode* p = root;
        while (!sta.empty() || p != NULL) {
            if (p != NULL) {
                sta.push(p);
                p = p -> left;
            }
            else {
                TreeNode* node = sta.top();
                sta.pop();
                result.push_back(node -> val);
                p = node -> right;
            }
        }

        return result;
    }


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


int main() {
    TreeNode* root = new TreeNode(2);
    root -> left = new TreeNode(3);
    root -> right = new TreeNode(4);
    root -> left -> left = new TreeNode(6);
    root -> left -> right = new TreeNode(5);
    root -> right -> right = new TreeNode(7);

    Solution sol;
    std::vector<int> result;

    result = sol.preorderTraversal(root);
    cout << "Pre order traversal:" << endl;
    for(auto i: result) cout << i << "  " ;
    cout << endl;

    result = sol.inorderTraversal(root);
    cout << "In order traversal:" << endl;
    for(auto i: result) cout << i << "  " ;
    cout << endl;

    result = sol.postorderTraversal(root);
    cout << "Post order traversal:" << endl;
    for(auto i: result) cout << i << "  " ;
    cout << endl;

    return 0;
}
