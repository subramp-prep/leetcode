class Solution {
    set<int> s;
    bool dfs(TreeNode *cur, int k) {
        if (!cur) return false;
        if (s.count(k - cur->val)) return true;
        s.insert(cur->val);
        return dfs(cur->left, k) || dfs(cur->right, k);
    }
public:
    bool findTarget(TreeNode* root, int k) {
        s.clear();
        return dfs(root, k);
    }
};