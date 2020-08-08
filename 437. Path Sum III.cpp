// 437. Path Sum III

/**
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
*/

#include <iostream>
using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int pathSum1(TreeNode* root, int sum) {
        if (root == nullptr) return 0;
        int cnt = helper(root, sum);
        
        return cnt + pathSum(root -> left, sum) + pathSum(root -> right, sum);
    }
    
private:
    int helper(TreeNode* root, int sum) {
        if (root == nullptr) return 0;
        
        sum -= root -> val;
        
        int cnt = (sum == 0 ? 1 : 0) + helper(root -> left, sum)
            + helper(root -> right, sum);
        return cnt;
    }
    
public:
    // use prefix sum
    int pathSum(TreeNode* root, int sum) {
        k = sum;
        map[0] = 1;
        preorder(root, 0);
        return cnt;
    }
private:
    int k;
    int cnt = 0;
    unordered_map<int, int> map;
    void preorder(TreeNode* node, int curSum) {
        if (node == nullptr) return;
        
        curSum += node -> val;
        
        cnt += map[curSum - k];
        map[curSum] += 1;
        preorder(node -> left, curSum);
        preorder(node -> right, curSum);
        map[curSum] -= 1; // remove current sum in order not to use it in parallel subtree processing
    }
};

int main() {
    TreeNode* n1 = new TreeNode(1);
    int sum = 2;

    n1 -> left = new TreeNode(2);

    Solution sol;
    cout << sol.pathSum1(n1, sum) << endl;
    cout << sol.pathSum(n1, sum) << endl;

    delete n1;
}
