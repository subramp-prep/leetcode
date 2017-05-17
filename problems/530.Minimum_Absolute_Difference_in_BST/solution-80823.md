Two Solutions, in-order traversal and a more general way using TreeSet | LeetCode Discuss
============================
**Author:**  shawngao
**Reputation:**  1164 

<p>The most common idea is to first <code>inOrder</code> traverse the tree and compare the delta between each of the adjacent values. It's guaranteed to have the correct answer because it is a <code>BST</code> thus <code>inOrder</code> traversal values are <code>sorted</code>.</p>
<p>Solution 1 - In-Order traverse, time complexity O(N), space complexity O(1).</p>
<pre><code>public class Solution {
    int min = Integer.MAX_VALUE;
    Integer prev = null;
    
    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;
        
        getMinimumDifference(root.left);
        
        if (prev != null) {
            min = Math.min(min, root.val - prev);
        }
        prev = root.val;
        
        getMinimumDifference(root.right);
        
        return min;
    }
    
}
</code></pre>
<p>What  if it is not a <code>BST</code>? (Follow up of the problem) The idea is to put values in a TreeSet and then every time we can use <code>O(lgN)</code> time to lookup for the nearest values.</p>
<p>Solution 2 - Pre-Order traverse, time complexity O(NlgN), space complexity O(N).</p>
<pre><code>public class Solution {
    TreeSet&lt;Integer&gt; set = new TreeSet&lt;&gt;();
    int min = Integer.MAX_VALUE;
    
    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;
        
        if (!set.isEmpty()) {
            if (set.floor(root.val) != null) {
                min = Math.min(min, root.val - set.floor(root.val));
            }
            if (set.ceiling(root.val) != null) {
                min = Math.min(min, set.ceiling(root.val) - root.val);
            }
        }
        
        set.add(root.val);
        
        getMinimumDifference(root.left);
        getMinimumDifference(root.right);
        
        return min;
    }
}
</code></pre> 

Ref: https://discuss.leetcode.com/topic/80823
