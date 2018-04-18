#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int racecar(int target) {
        int dp[target + 1];
        for (int i = 0; i <= target; ++i) {
            int n = floor(log2(i)) + 1;
            if (1 << n == i + 1) {
                dp[i] = n;
                continue;
            }
            dp[i] = dp[(1 << n) - 1 - i] + n + 1;
            for (int m = 0; m < n - 1; ++m)
                dp[i] = min(dp[i], dp[i - (1 << (n - 1)) + (1 << m)] + n + m + 1);
        }
        return dp[target];
    }
};


class Solution {
public:
    int dp[10001];
    int racecar(int t) {
        if (dp[t] > 0) return dp[t];
        int n = floor(log2(t)) + 1, res;
        if (1 << n == t + 1) dp[t] = n;
        else {
            dp[t] = racecar((1 << n) - 1 - t) + n + 1;
            for (int m = 0; m < n - 1; ++m)
                dp[t] = min(dp[t], racecar(t - (1 << (n - 1)) + (1 << m)) + n + m + 1);
        }
        return dp[t];
    }
};