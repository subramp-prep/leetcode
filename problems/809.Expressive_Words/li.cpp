class Solution {
public:
    int expressiveWords(string S, vector<string>& words) {
        int res = 0;
        for (auto &W : words) if (check(S, W)) res++;
        return res;
    }

    bool check(string S, string W) {
        int i = 0, j = 0, n = S.size(), m = W.size();
        while (i < n && j < m) {
            while (i < n && j < m && S[i] == W[j]) {i++; j++;}
            while (i > 0 && i < n && S[i] == S[i - 1]) i++;
            if (i < 3 || S[i - 1] != S[i - 2] || S[i - 2] != S[i - 3]) break;
        }
        return i == n && j == m;
    }
};