class Solution {
    public int racecar(int target) {
        int[] dp = new int[target + 1];
        for (int i = 0; i <= target; ++i) {
            int n = (int)(Math.log(i) / Math.log(2)) + 1;
            if (1 << n == i + 1) {
                dp[i] = n;
                continue;
            }
            dp[i] = dp[(1 << n) - 1 - i] + n + 1;
            for (int m = 0; m < n - 1; ++m)
                dp[i] = Math.min(dp[i], dp[i - (1 << (n - 1)) + (1 << m)] + n + m + 1);
        }
        return dp[target];
    }
}

class Solution {
    private int[] dp = new int[10001];
    public int racecar(int t) {
        if (dp[t] > 0) return dp[t];
        int n = (int)(Math.log(t) / Math.log(2)) + 1;
        if (1 << n == t + 1) dp[t] = n;
        else {
            dp[t] = racecar((1 << n) - 1 - t) + n + 1;
            for (int m = 0; m < n - 1; ++m)
                dp[t] = Math.min(dp[t], racecar(t - (1 << (n - 1)) + (1 << m)) + n + m + 1);
        }
        return dp[t];
    }
}