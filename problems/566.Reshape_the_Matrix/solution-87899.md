Python Solutions | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  15142 

<h4><strong>Solution 1 - <code>NumPy</code></strong></h4>
<p>When I read "MATLAB", I immediately thought "NumPy". Thanks to <a class="plugin-mentions-a" href="https://discuss.leetcode.com/uid/51826">@fallcreek</a> for <code>tolist</code>, makes converting the result to the correct type easier than what I had originally.</p>
<pre><code>import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
</code></pre>
<h4><strong>Solution 2 - Oneliner</strong></h4>
<p>An ugly oneliner :-)</p>
<pre><code>def matrixReshape(self, nums, r, c):
    return nums if len(sum(nums, [])) != r * c else map(list, zip(*([iter(sum(nums, []))]*c)))
</code></pre>
<p>A more readable version of that:</p>
<pre><code>def matrixReshape(self, nums, r, c):
    flat = sum(nums, [])
    if len(flat) != r * c:
        return nums
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)
</code></pre>
<h4><strong>Solution 3 - <code>itertools</code></strong></h4>
<pre><code>def matrixReshape(self, nums, r, c):
    if r * c != len(nums) * len(nums[0]):
        return nums
    it = itertools.chain(*nums)
    return [list(itertools.islice(it, c)) for _ in xrange(r)]</code></pre> 

Ref: https://discuss.leetcode.com/topic/87899
