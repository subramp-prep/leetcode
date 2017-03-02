class Solution
{
public:
    int evalRPN(vector<string>& tokens)
    {
        stack<int> stk;
        for (int i = 0; i < tokens.size(); ++i)
        {
            if (isNumber(tokens[i]))
                stk.push(stoi(tokens[i]));
            else
            {
                int val1 = stk.top(); stk.pop();
                int val2 = stk.top(); stk.pop();
                switch (tokens[i][0])
                {
                    case '+' : stk.push(val2 + val1); break;
                    case '-' : stk.push(val2 - val1); break;
                    case '*' : stk.push(val2 * val1); break;
                    case '/' : stk.push(val2 / val1); break;
                }
            }
        }
        return stk.top();
    }
    
    bool isNumber(string s) {return isdigit(s[0]) || (s.size() > 1 && s[0] == '-');}
};