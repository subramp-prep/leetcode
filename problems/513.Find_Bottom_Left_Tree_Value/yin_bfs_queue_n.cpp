// Breath-first Search
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    int findBottomLeftValue(TreeNode* root)
    {
        queue<TreeNode*> que;
        que.push(root);
        
        int res = -1;
        while (!que.empty())
        {
            int size = que.size();
            for (int i = 0; i < size; ++i)
            {
                TreeNode* curr = que.front(); que.pop();
                if (i == 0) res = curr->val; 
                if (curr->left) que.push(curr->left);
                if (curr->right) que.push(curr->right);
            }
        }
        return res;
    }
};