// In-Order Traversal
// Time Complexity O(n)
// Space Complxity O(h)
class Solution {
private:
    int res = INT_MAX, prev = -1;
public:
    int getMinimumDifference(TreeNode* root) {
        if (root->left) getMinimumDifference(root->left);
        if (prev >= 0) res = min(res, root->val - prev);
        prev = root->val;
        if (root->right) getMinimumDifference(root->right);
        return res;
    }
};