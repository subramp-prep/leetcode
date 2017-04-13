// Depth-first Search
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    bool isSymmetric(TreeNode* root)
    {
        if (!root) return true;
        stack<pair<TreeNode*, TreeNode*>> stk;
        stk.push(make_pair(root->left, root->right));
        
        while (!stk.empty())
        {
            pair<TreeNode*, TreeNode*> curr = stk.top(); stk.pop();
            TreeNode* left = curr.first, *right = curr.second;
            if (!left && !right) continue;
            if (!left || !right) return false;
            if (left->val != right->val) return false;
            stk.push(make_pair(left->left, right->right));
            stk.push(make_pair(left->right, right->left));
        }
        return true;
    }
};