class Solution {
public:
    int countBinarySubstrings(string s) {
        int cur = 1, pre = 0, res = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) cur++;
            else {
                res += min(cur, pre);
                pre = cur;
                cur = 1;
            }
        }
        return res + min(cur, pre);
    }
};


class Solution {
public:
    int countBinarySubstrings(string s) {
        vector<int> c;
        int count = 1;
        for (int i = 1, n = s.size(); i <= n; ++i) {
            if (s[i] != s[i - 1]) c.push_back(count);
            count = s[i] == s[i - 1] ? count + 1 : 1;
        }
        int res = 0;
        for (int i = 1; i < c.size(); ++i) res += min(c[i - 1], c[i]);
        return res;
    }
};


