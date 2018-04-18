class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        if (!root) return NULL;
        root->left = pruneTree(root->left);
        root->right = pruneTree(root->right);
        if (!root->left && !root->right && root->val == 0) return NULL;
        return root;
    }

    TreeNode* pruneTree(TreeNode* root) {
        if (root) root->left = pruneTree(root->left), root->right = pruneTree(root->right);
        return (root && (root->left || root->right || root->val)) ? root : NULL;
    }
};