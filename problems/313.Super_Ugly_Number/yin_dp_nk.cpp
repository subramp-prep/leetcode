// DP
// Time Comlexity O(nk)
// Space Complexity O(n)
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        int l = primes.size();
        vector<int> dp(n, INT_MAX), idx(l, 0);
        dp[0] = 1;
        
        for (int i = 1; i < n; ++i)
        {
            for (int j = 0; j < l; ++j) dp[i] = min(dp[i], primes[j] * dp[idx[j]]);
            for (int k = 0; k < l; ++k) if (dp[i] == primes[k] * dp[idx[k]]) ++idx[k];
        }
        
        return dp[n - 1];
    }
};