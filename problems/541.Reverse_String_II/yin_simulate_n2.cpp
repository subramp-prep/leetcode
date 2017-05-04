// Simulate
// Time Complexity O(n^2)
// Space Complexity O(1)
class Solution {
public:
    string reverseStr(string s, int k) {
        for (int left = 0; left < s.size(); left += 2 * k)
            for (int i = left, j = min<int>(left + k - 1, s.size() -1); i < j; ++i, --j)
                swap(s[i], s[j]);
        return s;
    }
};