class Solution
{
public:
    bool isMatch(string s, string p)
    {
         /**
         * f[i][j]: if s[0..i-1] matches p[0..j-1]
         * if p[j - 1] != '*'
         *      f[i][j] = f[i - 1][j - 1] && s[i - 1] == p[j - 1]
         * if p[j - 1] == '*', denote p[j - 2] with x
         *      f[i][j] is true iff any of the following is true
         *      1) "x*" repeats 0 time and matches empty: f[i][j - 2]
         *      2) "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x && f[i - 1][j]
         * '.' matches any single character
         */

         int m = s.size(), n = p.size();
         vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
         
         // two empty sub strings
         dp[0][0] = true;
         
         // s[0..i-1]" not empty and p[0..-1] empty -> false
         for (int i = 1; i <= m; ++i) 
            dp[i][0] = false;
        
        // p[0..i-1] not empty and s[0..-1] empty -> p[0..i-1] should be of form : x*y*z*k*t*...
         for (int j = 1; j <= n; ++j) 
            dp[0][j] = j > 1 && '*' == p[j - 1] && dp[0][j - 2]; // <-> length > 1 && last char is * && the dp value two letters ahead is also true
         
         // whatever i, j now
         for (int i = 1; i <= m; ++i)
             for (int j = 1; j <= n; ++j)
                 if (p[j - 1] =='*') // p[0..j-1] ends with x*
                               // "x*" repeats 0 time and matches empty: dp[i][j - 2] (the value is still true if we ignore x*)
                    dp[i][j] = dp[i][j - 2]
                               // "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x && dp[i - 1][j] (without the current s char, value is true and current s char is x)
                               || (s[i - 1] == p[j - 2] || '.' == p[j - 2]) && dp[i - 1][j];
                 else
                            // check strict equality
                    dp[i][j] = dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || '.' == p[j - 1]);
        
         return dp[m][n];
    }
};