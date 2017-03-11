// Author: Han
// Question: 172. Factorial Trailing Zeroes
// Date: 2017-03-11
// Complexity: O(LogN)
// Count factor 5

#include <iostream>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int ret = 0;
        for(n /= 5; n; n/=5) ret += n;
        return ret;
    }
};


int main() {
    Solution s;
    cout << s.trailingZeroes2(5) << endl;
    return 0;
}


