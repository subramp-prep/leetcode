Python with Sorting | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  17713 

<p>Three accepted solutions and me rambling on about failed attempts :-D</p>
<br/>
<h2>Solution 1 <sup>(accepted in 1792, 1747, 1700 ms)</sup></h2>
<p>I just sort the numbers 1 to n using my custom comparison. To compare two numbers, I "left-shift" them both before comparing them. For example if n = 49999, then I left-shift numbers so they're five digits. That is, 42 becomes 42000 and 123 becomes 12300. In case of ties, e.g., 420 also becoming 42000, the stability of <code>sorted</code> keeps them in order.</p>
<pre><code>def lexicalOrder(self, n):
    top = 1
    while top * 10 &lt;= n:
        top *= 10
    def mycmp(a, b, top=top):
        while a &lt; top: a *= 10
        while b &lt; top: b *= 10
        return -1 if a &lt; b else b &lt; a
    return sorted(xrange(1, n+1), mycmp)
</code></pre>
<br/>
<h2>Solution 2 <sup>(accepted in 1268, 1508, 1320, 1356, 1336 ms)</sup></h2>
<pre><code>def lexicalOrder(self, n):
    withKeys = []
    for i in xrange(1, n+1):
        key = i
        while key &lt; 1000000:
            key *= 10
        withKeys.append(key * 10000000 + i)
    withKeys.sort()
    return [ki % 10000000 for ki in withKeys]
</code></pre>
<p>Here I combine each number with a left-aligned version of it, for example:</p>
<pre><code>     42  =&gt;  42000000000042
   4200  =&gt;  42000000004200
 123456  =&gt;  12345600123456
</code></pre>
<p>Then just sort these and then extract the lower parts.</p>
<br/>
<h2>Complexity</h2>
<p>I think <strong>Time</strong> complexity and <strong>space</strong> complexity are both <strong>O(n)</strong> (at least if sort does what I think it does, I'll check some more), and the space complexity has a low hidden factor.</p>
<p>The time and memory limits for Python for this problem are pretty low, requiring a fairly efficient solution. On LeetCode, Python ints are 64 bits, so embedding the left-aligned version of numbers in the numbers (solution 2) doesn't cost extra memory. Also, sorting simple ints is fast. Especially since the order from 1 to n is already largely sorted lexicographically, like the streak from 100 to 999 and the streak from 1000 to 9999. And Python's (Tim)sort can take advantage of those streaks and just merge them. If it merges "left to right" like I think it does, then it merges the small streaks first and only integrates the longest streaks last, which leads to overall O(n) time.</p>
<br/>
<h2>Optimizing Solution 2 <sup>(accepted in 980, 984, 980 ms)</sup></h2>
<p>Instead of assuming that we get numbers up to seven digits long and using constants, this uses the largest power of 10 up to n.</p>
<pre><code>def lexicalOrder(self, n):
    highDigit = 1
    while highDigit * 10 &lt;= n:
        highDigit *= 10
    higherDigit = highDigit * 10
    withKeys = []
    for i in xrange(1, n+1):
        key = i
        while key &lt; highDigit:
            key *= 10
        withKeys.append(key * higherDigit + i)
    withKeys.sort()
    return [ki % higherDigit for ki in withKeys]
</code></pre>
<br/>
<h2>History...</h2>
<p>Of course the first thing I had tried was this:</p>
<pre><code>def lexicalOrder(self, n):
    return sorted(range(1, n+1), key=str)
</code></pre>
<p>Outrageously, this wasn't accepted! Got "Memory Limit Exceeded" at input n=49999! So next I tried the <code>cmp</code>-version of <code>sorted</code> instead of the <code>key</code>-version, and building strings only on the fly so it takes less memory:</p>
<pre><code>def lexicalOrder(self, n):
    return sorted(range(1, n+1), lambda a, b: cmp(str(a), str(b)))
</code></pre>
<p>Horrendously, this wasn't accepted! Got "Time Limit Exceeded" at input n=49999! So next I tried converting to strings, sorting those, and converting back to ints. Uses more memory, but less time:</p>
<pre><code>def lexicalOrder(self, n):
    return map(int, sorted(map(str, xrange(1, n+1))))
</code></pre>
<p>Unfathomably, this wasn't accepted! Got "Memory Limit Exceeded" at input n=49999! The horror! Apparently LeetCode really didn't want me to get away with being lazy. So I tried it without sorting or strings and built the numbers in correct order:</p>
<pre><code>def lexicalOrder(self, n):
    def dfs(i):
        if i &lt;= n:
            result.append(i)
            for d in xrange(10):
                dfs(10 * i + d)
    result = []
    for i in range(1, 10):
        dfs(i)
    return result
</code></pre>
<p>Irritatingly, this wasn't accepted! Got "Time Limit Exceeded"! At input n=<strong>14959</strong>! So it was even <strong>slower</strong> than the above. Geez. And none of this was even remotely close to the "5,000,000" that the problem threatened me with. I gave up. And implemented that last solution in C++. It got accepted.</p>
<p>Later I found out that the "5,000,000" isn't even close to true, the largest actual test case is 49999. But even after lots of different attempts, I still can't get any simple stringify+sort solution accepted. The most efficient I came up with is this:</p>
<pre><code>def lexicalOrder(self, n):
    return sorted(xrange(1, n+1), lambda a, b, s=str: 1 if s(b) &lt; s(a) else -1)
</code></pre>
<p>That uses <code>xrange</code>, which is faster than <code>range</code>, uses the <code>cmp</code>-version of <code>sorted</code> because the <code>key</code> version gets memory limit exceeded, uses a fast local variable instead of the slower global <code>str</code>, and exploits that there are no duplicate numbers so I just have to distinguish two cases which I do with <code>&lt;</code> instead of the <code>cmp</code> function. Still, after all of that optimization it's not fast enough. But based on comparing it with accepted solutions in custom testing, I think it's close. Maybe 10% too slow.</p>
<p>I did get one stringify+sort solution accepted, but it's less simple. I'll post that one later...</p> 

Ref: https://discuss.leetcode.com/topic/55090
