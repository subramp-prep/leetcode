6 lines Python / Ruby | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  14265

<p>Build the list of permutations one number at a time, insert the number into each already built permutation but only <strong>before</strong> other instances of the same number, never after. Inspired by <a href="https://leetcode.com/discuss/77245/line-python-solution-with-line-handle-duplication-beat-others" rel="nofollow">cbmbbz's already good solution</a>, though I then saw others had used the idea earlier.</p>
<hr/>
<h2>Python solution</h2>
<p>To find the last index for inserting new number <code>n</code> into old permutation <code>p</code>, I search for previous instances of <code>n</code> in <code>p</code>. But because <code>index</code> throws an exception if unsuccessful, I add a <a href="https://en.wikipedia.org/wiki/Sentinel_value" rel="nofollow">sentinel</a> <code>n</code> at the end (which is the appropriate last insertion index then).</p>
<pre><code>def permuteUnique(self, nums):
    perms = [[]]
    for n in nums:
        perms = [p[:i] + [n] + p[i:]
                 for p in perms
                 for i in xrange((p + [n]).index(n) + 1)]
    return perms
</code></pre>
<p>Or as "one-liner" using <code>reduce</code>:</p>
<pre><code>def permuteUnique(self, nums):
    return reduce(lambda perms, n: [p[:i] + [n] + p[i:]
                                    for p in perms
                                    for i in xrange((p + [n]).index(n) + 1)],
                  nums, [[]])
</code></pre>
<hr/>
<h2>Ruby solution</h2>
<pre><code>def permute_unique(nums)
  nums.reduce([[]]) { |perms, n|
    perms.flat_map { |p|
      last = p.index(n) || p.size
      (0..last).map { |i| p[0,i] + [n] + p[i..-1] }
    }
  }
end</code></pre>

Ref: https://discuss.leetcode.com/topic/33697/6-lines-python-ruby
