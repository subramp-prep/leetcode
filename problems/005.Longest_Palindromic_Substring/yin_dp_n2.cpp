class Solution {
public:
    string longestPalindrome(string s)
    {
        int n = s.size();
        string res = "";
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        
        for (int i = n - 1; i >= 0; --i) // Pay attention to the order here, because we have skipped the initilization : (i in n-1:0 and j in i:n-1) OR (i in 0:n-1 and j in i:0)
            for (int j = i; j < n; ++j)
            {
                dp[i][j] = (s[i] == s[j] && (j - i < 3 || dp[i + 1][j - 1])); // j - i < 3 : "a", "aa", "aba"
                if (dp[i][j] && j - i + 1 >= res.size()) { res = s.substr(i, j - i + 1); };
            }
        return res;
    }
};