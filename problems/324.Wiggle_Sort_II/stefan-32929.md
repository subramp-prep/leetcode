O(n)+O(1) after median --- Virtual Indexing | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  15574 

<p>This post is mainly about what I call "virtual indexing" technique (I'm sure I'm not the first who came up with this, but I couldn't find anything about it, so I made up a name as well. If you know better, let me know).</p>
<hr/>
<h2>Solution</h2>
<pre><code>void wiggleSort(vector&lt;int&gt;&amp; nums) {
    int n = nums.size();
    
    // Find a median.
    auto midptr = nums.begin() + n / 2;
    nth_element(nums.begin(), midptr, nums.end());
    int mid = *midptr;
    
    // Index-rewiring.
    #define A(i) nums[(1+2*(i)) % (n|1)]

    // 3-way-partition-to-wiggly in O(n) time with O(1) space.
    int i = 0, j = 0, k = n - 1;
    while (j &lt;= k) {
        if (A(j) &gt; mid)
            swap(A(i++), A(j++));
        else if (A(j) &lt; mid)
            swap(A(j), A(k--));
        else
            j++;
    }
}
</code></pre>
<hr/>
<h2>Explanation</h2>
<p>First I find a median using <code>nth_element</code>. That only guarantees O(n) <strong>average</strong> time complexity and I don't know about space complexity. I might write this myself using O(n) time and O(1) space, but that's not what I want to show here.</p>
<p>This post is about what comes <strong>after</strong> that. We can use <a href="https://en.wikipedia.org/wiki/Dutch_national_flag_problem#Pseudocode" rel="nofollow">three-way partitioning</a> to arrange the numbers so that those <em>larger than</em> the median come first, then those <em>equal to</em> the median come next, and then those <em>smaller than</em> the median come last.</p>
<p>Ordinarily, you'd then use one more phase to bring the numbers to their final positions to reach the overall wiggle-property. But I don't know a nice O(1) space way for this. Instead, I embed this right into the partitioning algorithm. That algorithm simply works with indexes 0 to n-1 as usual, but sneaky as I am, I rewire those indexes where I want the numbers to actually end up. The partitioning-algorithm doesn't even know that I'm doing that, it just works like normal (it just uses <code>A(x)</code> instead of <code>nums[x]</code>).</p>
<p>Let's say <code>nums</code> is <code>[10,11,...,19]</code>. Then after nth_element and ordinary partitioning, we might have this (15 is my median):</p>
<pre><code>index:     0  1  2  3   4   5  6  7  8  9
number:   18 17 19 16  15  11 14 10 13 12
</code></pre>
<p>I rewire it so that the first spot has index 5, the second spot has index 0, etc, so that I might get this instead:</p>
<pre><code>index:     5  0  6  1  7  2  8  3  9  4
number:   11 18 14 17 10 19 13 16 12 15
</code></pre>
<p>And 11 18 14 17 10 19 13 16 12 15 is perfectly wiggly. And the whole partitioning-to-wiggly-arrangement (everything after finding the median) only takes O(n) time and O(1) space.</p>
<hr/>
<p>If the above description is unclear, maybe this explicit listing helps:</p>
<p>Accessing <code>A(0)</code> actually accesses <code>nums[1]</code>.<br/>
Accessing <code>A(1)</code> actually accesses <code>nums[3]</code>.<br/>
Accessing <code>A(2)</code> actually accesses <code>nums[5]</code>.<br/>
Accessing <code>A(3)</code> actually accesses <code>nums[7]</code>.<br/>
Accessing <code>A(4)</code> actually accesses <code>nums[9]</code>.<br/>
Accessing <code>A(5)</code> actually accesses <code>nums[0]</code>.<br/>
Accessing <code>A(6)</code> actually accesses <code>nums[2]</code>.<br/>
Accessing <code>A(7)</code> actually accesses <code>nums[4]</code>.<br/>
Accessing <code>A(8)</code> actually accesses <code>nums[6]</code>.<br/>
Accessing <code>A(9)</code> actually accesses <code>nums[8]</code>.</p>
<hr/>
<p>Props to <a href="https://leetcode.com/discuss/77053/time-and-cheating-space-solution-will-there-be-real-solution?show=77054#a77054" rel="nofollow">apolloydy's solution</a>, I knew the partitioning algorithm already but I didn't know the name. And apolloydy's idea to partition to reverse order happened to make the index rewiring simpler.</p> 

Ref: https://discuss.leetcode.com/topic/32929
