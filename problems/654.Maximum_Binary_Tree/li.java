public class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return construct(nums, 0, nums.length);
    }

    TreeNode construct(int[] nums, int l, int r) {
        if (l >= r) return null;
        int maxi = l;
        for (int i = l + 1; i < r; i++) if (nums[i] > nums[maxi]) maxi = i;
        TreeNode root = new TreeNode(nums[maxi]);
        root.left = construct(nums, l, maxi);
        root.right = construct(nums, maxi + 1, r);
        return root;
    }
}