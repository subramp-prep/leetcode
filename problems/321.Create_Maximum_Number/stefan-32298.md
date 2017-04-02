Short Python / Ruby / C++ | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  14464 

<p><strong>Python</strong></p>
<pre><code>def maxNumber(self, nums1, nums2, k):

    def prep(nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] &lt; num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]

    def merge(a, b):
        return [max(a, b).pop(0) for _ in a+b]

    return max(merge(prep(nums1, i), prep(nums2, k-i))
               for i in range(k+1)
               if i &lt;= len(nums1) and k-i &lt;= len(nums2))
</code></pre>
<p>Solved it on my own but now I see others already posted this idea. Oh well, at least it's short, particularly my <code>merge</code> function.</p>
<p>The last two lines can be combined, but I find it rather ugly and not worth it:<br/>
<code>for i in range(max(k-len(nums2), 0), min(k, len(nums1))+1))</code></p>
<hr/>
<p><strong>Ruby</strong></p>
<pre><code>def prep(nums, k)
  drop = nums.size - k
  out = [9]
  nums.each do |num|
    while drop &gt; 0 &amp;&amp; out[-1] &lt; num
      out.pop
      drop -= 1
    end
    out &lt;&lt; num
  end
  out[1..k]
end

def max_number(nums1, nums2, k)
  ([k-nums2.size, 0].max .. [nums1.size, k].min).map { |k1|
    parts = [prep(nums1, k1), prep(nums2, k-k1)]
    (1..k).map { parts.max.shift }
  }.max
end
</code></pre>
<hr/>
<p><strong>C++</strong></p>
<p>Translated it to C++ as well now. Not as short anymore, but still decent. And C++ allows different functions with the same name, so I chose to do that here to show how nicely the <code>maxNumber(nums1, nums2, k)</code> problem can be based on the problems <code>maxNumber(nums, k)</code> and <code>maxNumber(nums1, nums2)</code>, which would make fine problems on their own.</p>
<pre><code>vector&lt;int&gt; maxNumber(vector&lt;int&gt;&amp; nums1, vector&lt;int&gt;&amp; nums2, int k) {
    int n1 = nums1.size(), n2 = nums2.size();
    vector&lt;int&gt; best;
    for (int k1=max(k-n2, 0); k1&lt;=min(k, n1); ++k1)
        best = max(best, maxNumber(maxNumber(nums1, k1),
                                   maxNumber(nums2, k-k1)));
    return best;
}

vector&lt;int&gt; maxNumber(vector&lt;int&gt; nums, int k) {
    int drop = nums.size() - k;
    vector&lt;int&gt; out;
    for (int num : nums) {
        while (drop &amp;&amp; out.size() &amp;&amp; out.back() &lt; num) {
            out.pop_back();
            drop--;
        }
        out.push_back(num);
    }
    out.resize(k);
    return out;
}

vector&lt;int&gt; maxNumber(vector&lt;int&gt; nums1, vector&lt;int&gt; nums2) {
    vector&lt;int&gt; out;
    while (nums1.size() + nums2.size()) {
        vector&lt;int&gt;&amp; now = nums1 &gt; nums2 ? nums1 : nums2;
        out.push_back(now[0]);
        now.erase(now.begin());
    }
    return out;
}
</code></pre>
<p>An alternative for <code>maxNumber(nums1, nums2)</code>:</p>
<pre><code>vector&lt;int&gt; maxNumber(vector&lt;int&gt; nums1, vector&lt;int&gt; nums2) {
    vector&lt;int&gt; out;
    auto i1 = nums1.begin(), end1 = nums1.end();
    auto i2 = nums2.begin(), end2 = nums2.end();
    while (i1 != end1 || i2 != end2)
        out.push_back(lexicographical_compare(i1, end1, i2, end2) ? *i2++ : *i1++);
    return out;
}</code></pre> 

Ref: https://discuss.leetcode.com/topic/32298
