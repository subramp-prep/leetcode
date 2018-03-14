#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    int bestRotation(vector<int>& A) {
        int N = A.size();
        int change[20000] = {0};
        for (int i = 0; i < N; ++i) change[(i - A[i] + 1 + N) % N] -= 1;
        for (int i = 1; i < N; ++i) change[i] += change[i - 1] + 1;
        return distance(change, max_element(change, change + N));
    }
};


class Solution2 {
public:
    int bestRotation(vector<int>& A) {
        int N = A.size();
        int *change = new int[N]();
        for (int i = 0; i < N; ++i) change[(i - A[i] + 1 + N) % N] -= 1;
        for (int i = 1; i < N; ++i) change[i] += change[i - 1] + 1;
        int res  = distance(change, max_element(change, change + N));
        delete[] change;
        return res;
    }
};


class Solution3 {
public:
    int bestRotation(vector<int>& A) {
        int N = A.size();
        vector<int> change(N);
        for (int i = 0; i < N; ++i) change[(i - A[i] + 1 + N) % N] -= 1;
        for (int i = 1; i < N; ++i) change[i] += change[i - 1] + 1;
        return distance(change.begin(), max_element(change.begin(), change.end()));
    }
};

int main() {
    Solution s;
    int n[] = {2, 3, 1, 4, 0} ;
    vector<int> A(n, n + 5);
    cout << s.bestRotation(A) << endl;
}


