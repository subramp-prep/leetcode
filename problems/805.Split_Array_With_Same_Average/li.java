class Solution {
    public boolean splitArraySameAverage(int[] A) {
        int n = A.length, s = Arrays.stream(A).sum();
        for (int i = 1; i <= n / 2; ++i) if (s * i % n == 0 && find(A, s * i / n, i, 0)) return true;
        return false;
    }

    public boolean find(int[] A, int target, int k, int i) {
        if (k == 0) return target == 0;
        if (k + i > A.length) return false;
        return find(A, target - A[i], k - 1, i + 1) || find(A, target, k, i + 1);
    }
}