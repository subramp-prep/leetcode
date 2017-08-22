sorting and normal Python | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  17383 

<p><strong>Solution 1</strong>, annotate the matrix entries with coordinate information so that we can just sort them by that.</p>
<pre><code>def findDiagonalOrder(self, matrix):
    entries = [(i+j, (j, i)[(i^j)&amp;1], val)
               for i, row in enumerate(matrix)
               for j, val in enumerate(row)]
    return [e[2] for e in sorted(entries)]
</code></pre>
<p>I just saw that <a class="plugin-mentions-a" href="https://discuss.leetcode.com/uid/110898">@_aig_</a> does it very similarly, <a href="https://discuss.leetcode.com/topic/77889/3-line-python-solution">but sorting coordinates</a>. Not sure what I like better.</p>
<p><strong>Solution 2</strong>, just walk over the matrix in the desired order. My <code>d</code> is the diagonal number, i.e., <code>i+j</code>. So I can compute <code>j</code> as <code>d-i</code>.</p>
<pre><code>def findDiagonalOrder(self, matrix):
    m, n = len(matrix), len(matrix and matrix[0])
    return [matrix[i][d-i]
            for d in range(m+n-1)
            for i in range(max(0, d-n+1), min(d+1, m))[::d%2*2-1]]
</code></pre>
<p>Why the range <code>range(max(0, d-n+1), min(d+1, m))</code>? Well I need <code>0 &lt;= i &lt; m</code> and <code>0 &lt;= j &lt; n</code>. As said above, <code>j</code> is <code>d-i</code>, so I have <code>0 &lt;= d-i &lt; n</code>. Isolating <code>i</code> gives me <code>i &lt;= d</code> and <code>i &gt; d-n</code>. Since we're dealing with integers, they're equivalent to <code>i &lt; d+1</code> and <code>i &gt;= d-n+1</code>. So my <code>i</code> needs to be in the range [0, m) as well as in the range [d-n+1, d+1). And my range is simply the intersection of those two ranges.</p> 

Ref: https://discuss.leetcode.com/topic/77933
