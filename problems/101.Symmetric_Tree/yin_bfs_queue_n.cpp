// Breath-first Search + Queue
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    bool isSymmetric(TreeNode* root)
    {
        // Init
        if (!root) return true;
        queue<TreeNode*> q1, q2;
        q1.push(root->left);
        q2.push(root->right);
        
        while (!q1.empty() && !q2.empty())
        {
            TreeNode* left = q1.front(); q1.pop();
            TreeNode* right = q2.front(); q2.pop();
            if (!left && !right) continue;
            if (!left || !right) return false;
            if (left->val != right->val) return false;
            q1.push(left->left);
            q1.push(left->right);
            q2.push(right->right);
            q2.push(right->left);
        }
        return q1.empty() && q2.empty();
    }
};