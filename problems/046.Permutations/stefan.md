One-Liners in Python | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  14265

<p><strong>Solution 1: <em>Recursive, take any number as first</em></strong></p>
<p>Take any number as the first number and append any permutation of the other numbers.</p>
<pre><code>def permute(self, nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
</code></pre>
<hr/>
<p><strong>Solution 2: <em>Recursive, insert first number anywhere</em></strong></p>
<p>Insert the first number anywhere in any permutation of the remaining numbers.</p>
<pre><code>def permute(self, nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]
</code></pre>
<hr/>
<p><strong>Solution 3: <em>Reduce, insert next number anywhere</em></strong></p>
<p>Use <code>reduce</code> to insert the next number anywhere in the already built permutations.</p>
<pre><code>def permute(self, nums):
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p)+1)],
                  nums, [[]])
</code></pre>
<hr/>
<p><strong>Solution 4: <em>Using the library</em></strong></p>
<pre><code>def permute(self, nums):
    return list(itertools.permutations(nums))
</code></pre>
<p>That returns a list of tuples, but the OJ accepts it anyway. If needed, I could easily turn it into a list of lists:</p>
<pre><code>def permute(self, nums):
    return map(list, itertools.permutations(nums))</code></pre>

Ref: https://discuss.leetcode.com/topic/17277/one-liners-in-python
