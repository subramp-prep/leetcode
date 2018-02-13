/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// 局部变量+指针
class Solution {
  public:
    int minDiffInBST(TreeNode* root) {
        int res = INT_MAX, pre = -1;
        helper(root, pre, res);
        return res;
    }

    void helper(TreeNode* root, int& pre, int& res) {
        if (root == NULL) return;
        helper(root->left, pre, res);
        if (pre >= 0) res = min(res, root->val - pre);
        pre = root->val;
        helper(root->right, pre, res);
    }
};


// 全局变量, no helper
class Solution {
  public:
    int res = INT_MAX, pre = -1;
    int minDiffInBST(TreeNode* root) {
        if (root->left != NULL) minDiffInBST(root->left);
        if (pre >= 0) res = min(res, root->val - pre);
        pre = root->val;
        if (root->right != NULL) minDiffInBST(root->right);
        return res;
    }
};