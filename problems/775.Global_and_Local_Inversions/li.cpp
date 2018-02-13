#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
        int cmax = 0, n = A.size();
        for (int i = 0; i < n - 2; ++i) {
            cmax = max(cmax, A[i]);
            if (cmax > A[i + 2]) return false;
        }
        return true;
    }
};



int main() {
    Solution s = Solution();
    int iarray[] = {0};
    size_t count = sizeof(iarray) / sizeof(int);
    vector<int> A(iarray, iarray + count);
    cout << s.isIdealPermutation(A) << endl;
}