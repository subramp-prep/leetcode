C++ 7 lines, O(n) run-time O(h) memory | LeetCode Discuss
============================
**Author:**  votrubac
**Reputation:**  70 

<p>In-order traversal of BST yields sorted sequence. So, we just need to subtract the previous element from the current one, and keep track of the minimum. We need O(1) memory as we only store the previous element, but we still need O(h) for the stack.</p>
<pre><code>void inorderTraverse(TreeNode* root, int&amp; val, int&amp; min_dif) {
    if (root-&gt;left != NULL) inorderTraverse(root-&gt;left, val, min_dif);
    if (val &gt;= 0) min_dif = min(min_dif, root-&gt;val - val);
    val = root-&gt;val;
    if (root-&gt;right != NULL) inorderTraverse(root-&gt;right, val, min_dif);
}
int getMinimumDifference(TreeNode* root) {
    auto min_dif = INT_MAX, val = -1;
    inorderTraverse(root, val, min_dif);
    return min_dif;
}
</code></pre>
<p>Another solution with the member variables (6 lines):</p>
<pre><code>class Solution {
    int min_dif = INT_MAX, val = -1;
public:
int getMinimumDifference(TreeNode* root) {
    if (root-&gt;left != NULL) getMinimumDifference(root-&gt;left);
    if (val &gt;= 0) min_dif = min(min_dif, root-&gt;val - val);
    val = root-&gt;val;
    if (root-&gt;right != NULL) getMinimumDifference(root-&gt;right);
    return min_dif;
}
</code></pre> 

Ref: https://discuss.leetcode.com/topic/80836
