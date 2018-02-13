class Solution {
    public boolean isIdealPermutation(int[] A) {
        int cmax = 0;
        for (int i = 0; i < A.size() - 2; ++i) {
            cmax = Math.max(cmax, A[i]);
            if (cmax > A[i + 2]) return false;
        }
        return true;
    }
}