/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
 public:
  TreeNode *pre = NULL;
  int res = INT_MAX;
  void inOrder(TreeNode *root) {
    if (!root) return;
    inOrder(root->left);
    if (pre) res = min(res, root->val - pre->val);
    pre = root;
    inOrder(root->right);
  }
  int getMinimumDifference(TreeNode *root) {
    inOrder(root);
    return res;
  }
};