// Dynamic programming
// Time Complexity O(n^2)
// Space Complexity O(n)
class Solution {
public:
    int numTrees(int n) {
        // init dp
        vector<int> dp(n + 1, 0);
        dp[0] = dp[1] = 1;
        // update dp
        for (int i = 2; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                dp[i] += dp[j] * dp[i - j - 1];
            }
        }
        return dp[n];
    }
};