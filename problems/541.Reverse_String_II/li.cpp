// Author: Jianghan LI
// Question: 541.Reverse_String_II
// Date: 2017-05-04 8:54 - 9:06

class Solution {
public:
    string reverseStr(string s, int k) {
        for (int i = 0; i < s.length(); i += 2 * k) {
            int tail = min(i + k - 1, int(s.length()) - 1);
            for(int j = 0; i + j < tail - j; j++) {
                swap(s[i + j], s[tail - j]);
            }
        }
        return s;
    }
};
