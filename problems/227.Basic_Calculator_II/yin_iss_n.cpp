class Solution {
public:
    int calculate(string s)
    {
        istringstream iss("+" + s + "+");
        int res = 0, term = 0, n;
        char op;
        while (iss >> op)
        {
            iss >> n; // get number
            switch (op) // operators
            {
                case '+' : res += term; term = n; break;
                case '-' : res += term; term = -n; break;
                case '*' : term *= n; break;
                case '/' : term /= n; break;
            }
        }
        return res;
    }
};