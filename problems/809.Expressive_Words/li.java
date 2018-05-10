class Solution {
    public int expressiveWords(String S, String[] words) {
        int res = 0;
        for (String W : words) if (check(S, W)) res++;
        return res;
    }
    public boolean check(String S, String W) {
        int i = 0, j = 0, n = S.length(), m = W.length();
        while (i < n && j < m) {
            while (i < n && j < m && S.charAt(i) == W.charAt(j)) {i++; j++;}
            if (i == n && j == m) return true;
            while (i > 0 && i < n && S.charAt(i) == S.charAt(i - 1)) i++;
            if (i < 3 || S.charAt(i - 1) != S.charAt(i - 2) || S.charAt(i - 2) != S.charAt(i - 3)) return false;
        }
        return i == n && j == m;
    }
}
