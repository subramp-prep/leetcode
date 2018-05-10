class Solution {
public:
    vector<string> ambiguousCoordinates(string S) {
        vector<string> ans;
        string str = S.substr(1, S.size()-2);
        int n = str.size();
        for (int i = 1; i < n; ++i) {
            vector<string> left = helper(str, 0, i);
            vector<string> right = helper(str, i, n);
            for (string& l: left) {
                for (string& r: right) {
                    ans.push_back("(" + l + ", " + r + ")");
                }
            }
        }
        return ans;
    }
    vector<string> helper(string& s, int start, int end) {
        vector<string> ans;
        if (start >= end) return ans;
        for (int i = start+1; i < end; ++i) {
            string left = s.substr(start, i-start), right = s.substr(i, end-i);
            if (right.back() == '0' || (left[0] == '0' && left.size() > 1)) continue;
            ans.push_back(left + '.' + right);
        }
        if (s[start] != '0' || end - start == 1)
            ans.push_back(s.substr(start, end-start));
        return ans;
    }
};