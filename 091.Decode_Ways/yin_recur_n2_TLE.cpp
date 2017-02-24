class Solution {
public:
    int numDecodings(string s)
    {
        if (s.empty()) return 0;
        return helper(s);
    }
    
    int helper(string s)
    {
        int n = s.size();
        if (n == 0) return 1;
        if (n == 1) return (s[0] > '0');
        int val = stoi(s.substr(n - 2, 2));
        return helper(s.substr(0, n - 2)) * (val >= 10 && val <= 26) + helper(s.substr(0, n - 1)) * (s[n - 1] > '0');
    }
};