class Solution {
public:
    string longestPalindrome(string s)
    {
        if (s.empty()) return "";
        if (s.size() == 1) return s;
        int start = 0, max_len = 1, i = 0;
        while (i < s.size())
        {
            if (s.size() - i <= max_len / 2) break;
            int l = i, r = i;
            while (s[r + 1] == s[r]) ++r; // skip duplications
            while (l > 0 && r + 1 < s.size() && s[r + 1] == s[l - 1]) { --l; ++r; } // expand substring
            if (r - l + 1 > max_len) { max_len = r - l + 1; start = l;} // update res;
            ++i;
        }
        return s.substr(start, max_len);
    }
};