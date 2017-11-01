// Go inorder and decrease k at each node.
// Stop the whole search as soon as k is zero,
// and then the k-th element is immediately returned all the way
// to the recursion top and to the original caller.

// Try the left subtree first. If that made k zero,
// then its answer is the overall answer and we return it right away.
// Otherwise, decrease k for the current node, and if that made k zero,
// then we return the current node's value right away.
// Otherwise try the right subtree and return whatever comes back from there.

int kthSmallest(TreeNode* root, int& k) {
    if (root) {
        int x = kthSmallest(root->left, k);
        return !k ? x : !--k ? root->val : kthSmallest(root->right, k);
    }
}
// You might notice that I changed k from int to int&
// because I didn't feel like adding a helper just for that
// and the OJ doesn't mind. Oh well, here is that now:

int kthSmallest(TreeNode* root, int k) {
    return find(root, k);
}
int find(TreeNode* root, int& k) {
    if (root) {
        int x = find(root->left, k);
        return !k ? x : !--k ? root->val : find(root->right, k);
    }
}