Short simple C++ | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  15574 

<pre><code>void wiggleSort(vector&lt;int&gt;&amp; nums) {
    vector&lt;int&gt; sorted(nums);
    sort(sorted.begin(), sorted.end());
    for (int i=nums.size()-1, j=0, k=i/2+1; i&gt;=0; i--)
        nums[i] = sorted[i&amp;1 ? k++ : j++];
}
</code></pre>
<p>Sort and then write the smaller half of the numbers on the even indexes and the larger half of the numbers on the odd indexes, both from the back. Example:</p>
<pre><code>Small half:    4 . 3 . 2 . 1 . 0 .
Large half:    . 9 . 8 . 7 . 6 . 5
----------------------------------
Together:      4 9 3 8 2 7 1 6 0 5
</code></pre>
<p>So write <code>nums</code> from the back, interweaving <code>sorted[0..4]</code> (indexed by <code>j</code>) and <code>sorted[5..9]</code> (indexed by <code>k</code>).</p>
<p>For more explanation/proof, see <a href="https://leetcode.com/discuss/76965/3-lines-python-with-explanation-proof" rel="nofollow">my equivalent Python solution</a>.</p> 

Ref: https://discuss.leetcode.com/topic/32882
