class Solution {
public:
    int numDecodings(string s)
    {
        if (s.empty()) return 0;
        
        int n = s.size();
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // init

        // update dp[i + 1]
        for (int i = 0; i < n; ++i)
        {
            // xxxxn
            dp[i + 1] = dp[i] * (s[i] > '0'); 
            if (i == 0) continue;
            
            // xxxnn
            int val = stoi(s.substr(i - 1, 2));
            dp[i + 1] += dp[i - 1] * (val >= 10 && val <= 26);
        }
        return dp[n];
    }
};