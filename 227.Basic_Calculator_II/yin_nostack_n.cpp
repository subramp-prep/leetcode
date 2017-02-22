class Solution {
public:
    int calculate(string s)
    {
        s = "+" + s;
        int res = 0, term = 0;
        for (int i = 0; i < s.size();)
        {
            char op = s[i++];
            while (isspace(s[i])) ++i; // skip spaces
            
            // get number
            int j = i;
            while (isdigit(s[i])) ++i;
            int val = stoi(s.substr(j, i - j));
            
            // operators
            switch (op)
            {
                case '+' : res += term; term = val; break;
                case '-' : res += term; term = -val; break;
                case '*' : term *= val; break;
                case '/' : term /= val; break;
            }

            while (isspace(s[i])) ++i; // skip spaces
        }
        res += term;
        
        return res;
    }
};