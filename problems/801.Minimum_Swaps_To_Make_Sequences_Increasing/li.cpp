#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        int N = A.size();
        int not_swap[1000] = {0};
        int swap[1000] = {1};
        for (int i = 1; i < N; ++i) {
            not_swap[i] = swap[i] = N;
            if (A[i - 1] < A[i] && B[i - 1] < B[i]) {
                not_swap[i] = not_swap[i - 1];
                swap[i] = swap[i - 1] + 1;
            }
            if (A[i - 1] < B[i] && B[i - 1] < A[i]) {
                not_swap[i] = min(not_swap[i], swap[i - 1]);
                swap[i] = min(swap[i], not_swap[i - 1] + 1);
            }
        }
        return min(swap[N - 1], not_swap[N - 1]);
    }
};




int main() {
    Solution s;
    int a[4] = {1, 3, 5, 4};
    int b[] = {1, 2, 3, 7};
    vector<int> A(a, a + 4);
    vector<int> B(b, b + 4);
    cout << s.minSwap(A, B) << endl;
}