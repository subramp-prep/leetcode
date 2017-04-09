Pigeon hole principle | LeetCode Discuss
============================
**Author:**  morrischen2008
**Reputation:**  721 

<p>Suppose you have n pigeons with labels and you put them into m holes based on their label with each hole of the same size. Why bother putting pigeons into holes? Because you want to disregard the distance between pigeons <strong>within</strong> each one hole.</p>
<p>Only when at least one hole is empty can we disregard the distance between pigeons within each one hole and compute the maximum gap solely by the distance between pigeons <strong>in adjacent holes</strong>. We make sure that at least one hole is empty by using m=n-1 (i.e. n-2 pigeons in n-1 holes =&gt; at least one hole is empty).</p>
<pre><code>int maximumGap(vector&lt;int&gt;&amp; nums) {
        const int n = nums.size();
        if(n&lt;=1) return 0;
        int maxE = *max_element(nums.begin(),nums.end());
        int minE = *min_element(nums.begin(),nums.end());
        double len = double(maxE-minE)/double(n-1);
        vector&lt;int&gt; maxA(n,INT_MIN);
        vector&lt;int&gt; minA(n,INT_MAX);
        for(int i=0; i&lt;n; i++) {
            int index = (nums[i]-minE)/len;
            maxA[index] = max(maxA[index],nums[i]);
            minA[index] = min(minA[index],nums[i]);
        }
        int gap = 0, prev = maxA[0];
        for(int i=1; i&lt;n; i++) {
            if(minA[i]==INT_MAX) continue;
            gap = max(gap,minA[i]-prev);
            prev = maxA[i];
        }
        return gap;
    }</code></pre> 

Ref: https://discuss.leetcode.com/topic/13172
