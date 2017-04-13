// Depth-first Search
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    int findBottomLeftValue(TreeNode* root)
    {
        int h = -1, res;
        stack<pair<TreeNode*, int>> stk;
        stk.push(make_pair(root, 0));
        while (!stk.empty())
        {
            pair<TreeNode*, int> curr = stk.top(); stk.pop();
            if (h < curr.second)
            {
                h = curr.second;
                res = curr.first->val;
            }
            if (curr.first->right) stk.push(make_pair(curr.first->right, curr.second + 1));
            if (curr.first->left) stk.push(make_pair(curr.first->left, curr.second + 1));
        }
        return res;
    }
};