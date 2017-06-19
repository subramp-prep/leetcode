My short c++ solution, O(1) space, and O(n) time | LeetCode Discuss
============================
**Author:**  makuiyu
**Reputation:**  1089 

<p>Put each number in its right place.</p>
<p>For example:</p>
<p>When we find 5, then swap it with A[4].</p>
<p>At last, the first place where its number is not right, return the place + 1.</p>
<pre><code>class Solution
{
public:
    int firstMissingPositive(int A[], int n)
    {
        for(int i = 0; i &lt; n; ++ i)
            while(A[i] &gt; 0 &amp;&amp; A[i] &lt;= n &amp;&amp; A[A[i] - 1] != A[i])
                swap(A[i], A[A[i] - 1]);
        
        for(int i = 0; i &lt; n; ++ i)
            if(A[i] != i + 1)
                return i + 1;
        
        return n + 1;
    }
};</code></pre> 

Ref: https://discuss.leetcode.com/topic/8293
