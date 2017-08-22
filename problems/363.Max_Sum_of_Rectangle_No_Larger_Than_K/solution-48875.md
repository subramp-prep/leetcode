Accepted C++ codes with explanation and references | LeetCode Discuss
============================
**Author:**  java-chao
**Reputation:**  130 

<p>The naive solution is brute-force, which is O((mn)^2). In order to be more efficient, I tried something similar to Kadane's algorithm. The only difference is that here we have upper bound restriction K. Here's the easily understanding video link for the problem "find the max sum rectangle in 2D array": <a href="https://www.youtube.com/watch?v=yCQN096CwWM" rel="nofollow">Maximum Sum Rectangular Submatrix in Matrix dynamic programming/2D kadane</a> (Trust me, it's really easy and straightforward).</p>
<p>Once you are clear how to solve the above problem, the next step is to find the max sum no more than K in an array. This can be done within O(nlogn), and you can refer to this article: <a href="https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k" rel="nofollow">max subarray sum no more than k</a>.</p>
<p>For the solution below, I assume that the number of rows is larger than the number of columns. Thus in general time complexity is O[min(m,n)^2 * max(m,n) * log(max(m,n))], space O(max(m, n)).</p>
<pre><code>int maxSumSubmatrix(vector&lt;vector&lt;int&gt;&gt;&amp; matrix, int k) {
    if (matrix.empty()) return 0;
    int row = matrix.size(), col = matrix[0].size(), res = INT_MIN;
    for (int l = 0; l &lt; col; ++l) {
        vector&lt;int&gt; sums(row, 0);
        for (int r = l; r &lt; col; ++r) {
            for (int i = 0; i &lt; row; ++i) {
                sums[i] += matrix[i][r];
            }
            
            // Find the max subarray no more than K 
            set&lt;int&gt; accuSet;
            accuSet.insert(0);
            int curSum = 0, curMax = INT_MIN;
            for (int sum : sums) {
                curSum += sum;
                set&lt;int&gt;::iterator it = accuSet.lower_bound(curSum - k);
                if (it != accuSet.end()) curMax = std::max(curMax, curSum - *it);
                accuSet.insert(curSum);
            }
            res = std::max(res, curMax);
        }
    }
    return res;
}
</code></pre> 

Ref: https://discuss.leetcode.com/topic/48875
