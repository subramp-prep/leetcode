Short and Clear Solutions | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  15142 

<p>Straight-forward iterative solution:</p>
<pre><code>def subsets(self, nums):
    subsets = [[]]
    for n in sorted(nums):
        subsets += [s + [n] for s in subsets]
    return subsets
</code></pre>
<p>Same thing but with <code>reduce</code> instead of the loop:</p>
<pre><code>def subsets(self, nums):
    return reduce(lambda subsets, n: subsets + [s+[n] for s in subsets],
                  sorted(nums), [[]])
</code></pre>
<p>Using <code>combinations</code> from the library:</p>
<pre><code>def subsets(self, nums):
    return [s for n in range(len(nums)+1)
            for s in itertools.combinations(sorted(nums), n)]
</code></pre>
<p>Using integers as bit mask to tell which elements to use in a subset:</p>
<pre><code>def subsets(self, nums):
    nums.sort()
    return [[nums[i] for i in range(len(nums)) if mask &gt;&gt; i &amp; 1]
            for mask in range(2 ** len(nums))]</code></pre> 

Ref: https://discuss.leetcode.com/topic/15819
