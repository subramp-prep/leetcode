class Solution {
public:
    int calculate(string s)
    {
        s = "+" + s;
        
        stack<int> nums;
        for (int i = 0; i < s.size();)
        {
            char op = s[i++];
            while (isspace(s[i])) ++i; // skip spaces
            
            // get number between operators
            int j = i;
            while (isdigit(s[i])) ++i;
            int val = stoi(s.substr(j, i - j));
            
            // operators
            switch (op)
            {
                case '+' : break;
                case '-' : val *= -1; break;
                case '*' : val = nums.top() * val; nums.pop(); break;
                case '/' : val = nums.top() / val; nums.pop(); break;
            }
            nums.push(val);
            
            while (isspace(s[i])) ++i; // skip spaces
        }
        
        // build result
        int res = 0;
        while (!nums.empty())
        {
            res += nums.top();
            nums.pop();
        }
        return res;
    }
};