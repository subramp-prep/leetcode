Python and Java with little tricks (incl. a oneliner :-) | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  16161 

<p>Keeping track of the balance (number of ones minus number of zeros) and storing the first index where each balance occurred.</p>
<hr/>
<p><strong>Python</strong></p>
<p>Keeping the balance in units of 0.5 which makes the update expression short (not that <code>num * 2 - 1</code> or <code>1 if num else -1</code> would be terribly long):</p>
<pre><code>def findMaxLength(self, nums):
    index = {0: -1}
    balance = maxlen = 0
    for i, num in enumerate(nums):
        balance += num - 0.5
        maxlen = max(maxlen, i - index.setdefault(balance, i))
    return maxlen
</code></pre>
<p>Just for fun as an ugly one-liner:</p>
<pre><code>def findMaxLength(self, nums):
    return reduce(lambda(f,b,m),(i,x):(f,b+x-.5,max(m,i-f.setdefault(b+x-.5,i))),enumerate(nums),({0:-1},0,0))[2]
</code></pre>
<hr/>
<p><strong>Java</strong></p>
<p>Using <code>putIfAbsent</code> so I only need one map function call per number.</p>
<pre><code>public int findMaxLength(int[] nums) {
    Map&lt;Integer, Integer&gt; index = new HashMap&lt;&gt;();
    index.put(0, -1);
    int balance = 0, maxlen = 0;
    for (int i = 0; i &lt; nums.length; i++) {
        balance += nums[i] * 2 - 1;
        Integer first = index.putIfAbsent(balance, i);
        if (first != null)
            maxlen = Math.max(maxlen, i - first);
    }
    return maxlen;
}
</code></pre>
<p>Could avoid using <code>Math.max</code> like this:</p>
<pre><code>        if (first != null &amp;&amp; i - first &gt; maxlen)
            maxlen = i - first;</code></pre> 

Ref: https://discuss.leetcode.com/topic/79977
