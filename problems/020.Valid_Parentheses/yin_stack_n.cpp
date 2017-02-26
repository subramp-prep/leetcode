class Solution {
public:
    bool isValid(string s)
    {
        unordered_map<char, char> hash( {{')', '('}, {']', '['}, {'}', '{'}} );
        stack<char> parens;
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{')
            {
                parens.push(s[i]);
            }
            
            if (hash.find(s[i]) != hash.end())
            {
                if (parens.empty() || parens.top() != hash[s[i]])
                    return false;
                parens.pop();
            }
        }
        return parens.empty();
    }
};