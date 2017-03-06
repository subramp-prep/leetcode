// Stack
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    int calculate(string s)
    {
        stack<int> stk;
        int res = 0, sign = 1;
        for (int i = 0; i < s.size();)
        {
            if (isdigit(s[i])) // get the number
            {
                int j = i;
                while (isdigit(s[j])) ++j;
                res += sign * stoi(s.substr(i, j - i));
                i = j;
            }
            else
            {
                switch (s[i])
                {
                    // change sign
                    case '+' : sign = 1; break;
                    case '-' : sign = -1; break;
                    
                    // push current result and sign to stack
                    case '(' : stk.push(res); stk.push(sign); res = 0; sign = 1; break; 
                    
                    // combine current result and last result
                    case ')' :
                    {
                        int val1 = stk.top(); stk.pop();
                        int val2 = stk.top(); stk.pop();
                        res = res * val1 + val2;
                        break;
                    }
                }
                ++i;
            }
        }
        return res;
    }
};