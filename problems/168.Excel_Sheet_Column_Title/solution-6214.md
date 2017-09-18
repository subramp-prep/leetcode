My 1 lines code in Java, C++, and Python | LeetCode Discuss
============================
**Author:**  xcv58
**Reputation:**  1292 

<p>Java:</p>
<pre><code>return n == 0 ? "" : convertToTitle(--n / 26) + (char)('A' + (n % 26));
</code></pre>
<p>C++:</p>
<pre><code>return n == 0 ? "" : convertToTitle(n / 26) + (char) (--n % 26 + 'A');
</code></pre>
<p>update: because the behavior of different compilers, the safe version should be:</p>
<pre><code>return n == 0 ? "" : convertToTitle((n - 1) / 26) + (char) ((n - 1) % 26 + 'A');
</code></pre>
<p>Python:</p>
<pre><code>return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))</code></pre> 

Ref: https://discuss.leetcode.com/topic/6214
