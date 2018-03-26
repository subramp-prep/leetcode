class Solution {
public:
    bool splitArraySameAverage(vector<int>& A) {
        int n = A.size(), s = accumulate(A.begin(), A.end(), 0);
        for (int i = 1; i <= n / 2; ++i) if (s * i % n == 0 && find(A, s * i / n, i, 0)) return true;
        return false;
    }
    bool find(vector<int>& A, int target, int k, int i) {
        if (k == 0) return target == 0;
        if (k + i > A.size()) return false;
        return find(A, target - A[i], k - 1, i + 1) || find(A, target, k, i + 1);
    }
};