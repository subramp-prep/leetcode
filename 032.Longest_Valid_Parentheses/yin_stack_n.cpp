class Solution {
public:
    int longestValidParentheses(string s)
    {
        int n = s.size(), res = 0;
        stack<int> stk;
        stk.push(-1);
        
        // scan string
        for (int i = 0; i < n; ++i)
        {
            if (s[i] == '(') stk.push(i);
            else if (!stk.empty() && s[stk.top()] == '(')
            {
                stk.pop();
                res = max(res, i - stk.top());
            }
            else
                stk.push(i);
        }
        return res;
    }
};