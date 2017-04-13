// Depth-first Search
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    bool isSymmetric(TreeNode* root)
    {
        return !root || isSymmetric(root->left, root->right);
    }
    
    bool isSymmetric(TreeNode* left, TreeNode* right)
    {
        if (!left && !right) return true;
        if (!left || !right) return false;
        if (left->val != right->val) return false;
        return isSymmetric(left->left, right->right) && isSymmetric(left->right, right->left);
    }
};