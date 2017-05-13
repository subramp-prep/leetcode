Easy Python, ~230ms | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  15343 

<p>My <code>X</code> is the set of still available numbers. Gets accepted in about 230 ms:</p>
<pre><code>def countArrangement(self, N):
    def count(i, X):
        if i == 1:
            return 1
        return sum(count(i - 1, X - {x})
                   for x in X
                   if x % i == 0 or i % x == 0)
    return count(N, set(range(1, N + 1)))
</code></pre>
<p>Note that my <code>i</code> goes <strong>downwards</strong>, from N to 1. Because position <code>i = 1</code> can hold <strong>any</strong> number, so I don't even have to check whether the last remaining number fits there. Also, position <code>i = 2</code> happily holds every second number and <code>i = 3</code> happily holds every third number, so filling the lowest positions <strong>last</strong> has a relatively high chance of success. In other words, it's relatively hard to end up with dead ends this way.</p>
<p>If I go <strong>upwards</strong> (from 1 to N), it takes about 2300 ms:</p>
<pre><code>def countArrangement(self, N):
    def count(i, X):
        if i &gt; N:
            return 1
        return sum(count(i + 1, X - {x})
                   for x in X
                   if x % i == 0 or i % x == 0)
    return count(1, set(range(1, N + 1)))</code></pre> 

Ref: https://discuss.leetcode.com/topic/79968
