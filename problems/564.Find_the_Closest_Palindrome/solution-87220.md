Python, Simple with Explanation | LeetCode Discuss
============================
**Author:**  awice
**Reputation:**  146 

<p>Let's build a list of candidate answers for which the final answer must be one of those candidates.  Afterwards, choosing from these candidates is straightforward.</p>
<p>If the final answer has the same number of digits as the input string <code>S</code>, then the answer must be the middle digits + (-1, 0, or 1) flipped into a palindrome.  For example, <code>23456</code> had middle part <code>234</code>, and <code>233, 234, 235</code> flipped into a palindrome yields <code>23332, 23432, 23532</code>.  Given that we know the number of digits, the prefix <code>235</code> (for example) uniquely determines the corresponding palindrome <code>23532</code>, so all palindromes with larger prefix like <code>23732</code> are strictly farther away from S than <code>23532 &gt;= S</code>.</p>
<p>If the final answer has a different number of digits, it must be of the form <code>999....999</code> or <code>1000...0001</code>, as any palindrome smaller than <code>99....99</code> or bigger than <code>100....001</code> will be farther away from S.</p>
<pre><code>def nearestPalindromic(self, S):
    K = len(S)
    candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
    prefix = S[:(K+1)/2]
    P = int(prefix)
    for start in map(str, (P-1, P, P+1)):
        candidates.append(start + (start[:-1] if K%2 else start)[::-1])
    
    def delta(x):
        return abs(int(S) - int(x))
    
    ans = None
    for cand in candidates:
        if cand != S and not cand.startswith('00'):
            if (ans is None or delta(cand) &lt; delta(ans) or
                    delta(cand) == delta(ans) and int(cand) &lt; int(ans)):
                ans = cand
    return ans
</code></pre> 

Ref: https://discuss.leetcode.com/topic/87220
