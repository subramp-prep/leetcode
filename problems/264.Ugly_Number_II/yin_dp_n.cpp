// DP
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    int nthUglyNumber(int n) {
        // corner cases
        if (n <= 0) return 0;
        if (n == 1) return 1;
        int idx2 = 0, idx3 = 0, idx5 = 0;
        
        // dp init
        vector<int> dp(n);
        dp[0] = 1;
        
        // update dp
        for (int i = 1; i < n; ++i)
        {
            dp[i] = min(dp[idx2] * 2, min(dp[idx3] * 3, dp[idx5] * 5));
            if (dp[i] == dp[idx2] * 2) ++idx2;
            if (dp[i] == dp[idx3] * 3) ++idx3;
            if (dp[i] == dp[idx5] * 5) ++idx5;
        }
        return dp[n - 1];
    }
};