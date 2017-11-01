// Author: Jianghan LI
// Question: 344.Reverse_String
// Complexity: O(N)
// Date: 2017-09-29 10:12 - 10:13, 0 wrong try

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string reverseString(string s) {
        int n = s.size();
        char c;
        for (int i; i < n / 2; i++) {
            c = s[i];
            s[i] = s[n - 1 - i];
            s[n - 1 - i] = c;
        }
        return s;
    }
};

int main() {
    Solution s;
    cout << s.reverseString("hi") << endl; ‚
    return 0;
}