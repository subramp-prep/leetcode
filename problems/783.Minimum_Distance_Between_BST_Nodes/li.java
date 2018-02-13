/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    Integer res = Integer.MAX_VALUE, pre = null;

    public int minDiffInBST(TreeNode root) {
        inorder(root);
        return res;
    }

    public void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        if (pre != null) res = Math.min(res, root.val - pre);
        pre = root.val;
        inorder(root.right);
    }
}


// no helper
class Solution {
    Integer res = Integer.MAX_VALUE, pre = null;
    public int minDiffInBST(TreeNode root) {
        if (root.left != null) minDiffInBST(root.left);
        if (pre != null) res = Math.min(res, root.val - pre);
        pre = root.val;
        if (root.right != null) minDiffInBST(root.right);
        return res;
    }
}