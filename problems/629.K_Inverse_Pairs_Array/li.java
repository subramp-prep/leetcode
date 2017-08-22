// 2017.08.17  Jianghan LI
public class Solution {
    public int kInversePairs(int n, int k) {
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 0; i <= n; i++) dp[i][0] = 1;
        int M = 1000000007;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % M;
                if (j - i >= 0) dp[i][j] = (dp[i][j] + M - dp[i - 1][j - i]) % M;
            }
        }
        return dp[n][k];
    }
}