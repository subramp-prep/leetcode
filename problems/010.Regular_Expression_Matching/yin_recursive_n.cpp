class Solution
{
public:
    bool isMatch(string s, string p)
    {
        // end condition : p string empty -> s empty
        if (p.empty()) return s.empty();
        
        if (p.size() >= 2 && p[1] == '*')
            return isMatch(s, p.substr(2)) || // ignore the x* and go on, we admit an empty s here, because isMatch("", ".*") is also true
                   (!s.empty() && (p[0] == s[0] || p[0] == '.') && isMatch(s.substr(1), p)); // check equality, remove first char and go on
        else
            return !s.empty() && (p[0] == s[0] || p[0] == '.') && isMatch(s.substr(1), p.substr(1)); // check equality, remove first char and go on
    }
};