class Solution {
public:
    int longestValidParentheses(string s)
    {
        int n = s.size(), res = 0;
        // dp[i] : length of longest valid pars of s[0..i-1], dp[0] for empty string
        vector<int> dp (n + 1, 0); 
        
        for (int j = 1; j < n; ++j) // update dp[j + 1]
        {
            if (s[j] == ')')
            {
                // case "xxxx()"
                if (s[j - 1] == '(') dp[j + 1] = 2 + dp[j - 1];
                else 
                {
                    // case "xx(xx)"
                    int i = j - dp[j] - 1; // pos of left par
                    if (i >= 0 && s[i] =='(') dp[j + 1] = 2 + dp[j] + dp[i];
                }
                res = max(dp[j + 1], res);
            }
        }
        return res;
    }
};