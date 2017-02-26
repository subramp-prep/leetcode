class Solution {
public:
    int longestValidParentheses(string s)
    {
        int n = s.size(), res = 0;
        stack<int> stk;
        stk.push(-1); // 标志左侧起始点，保证了stack永远不空，也可以s = ')' + s

        // scan string
        for (int i = 0; i < n; ++i)
        {
            if (s[i] == '(') stk.push(i);
            else if (s[stk.top()] == '(')
            {
                stk.pop();
                res = max(res, i - stk.top());
            }
            else
                stk.push(i); // 可以不再考虑string是不是valid
        }
        return res;
    }
};