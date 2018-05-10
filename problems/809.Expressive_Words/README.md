809.Expressive_Words
----------------------------------------------
Problem: https://leetcode.com/problems/Expressive-Words
Solution: https://github.com/JianghanLi/LeetCode/problems/809.Expressive_Words
Discuss: https://leetcode.com/problems/expressive-words/discuss/122660/C++JavaPython-Two-Pointers


###**Discuss**：

[C++/Java/Python] Two Pointers

Loop through all words. ```check(string S, string W)``` checks if ```W``` is stretchy to ```S```.

In ```check``` function, use while loop and two pointer:
1. If ```S[i] == W[j]```, ```i++, j++```
2. If ```S[i] != W[j]```,  increase ```i``` until a different char.
3. Check at lesst 3 occurnce.



C++:
```
    int expressiveWords(string S, vector<string>& words) {
        int res = 0;
        for (auto &W : words) if (check(S, W)) res++;
        return res;
    }

    bool check(string S, string W) {
        int i = 0, j = 0, n = S.size(), m = W.size();
        while (i < n && j < m) {
            while (i < n && j < m && S[i] == W[j]) {i++; j++;}
            if (i == n && j == m) return true;
            while (i > 0 && i < n && S[i] == S[i - 1]) i++;
            if (i < 3 || S[i - 1] != S[i - 2] || S[i - 2] != S[i - 3]) return false;
        }
        return i == n && j == m;
    }
```
Java:
```
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
```
Python:
```
    def expressiveWords(self, S, words):
        def check(S, W):
            i, j, n, m = 0, 0, len(S), len(W)
            while i < n and j < m:
                while i < n and j < m and S[i] == W[j]: i, j = i + 1, j + 1
                if i == n and j == m: return True
                while i > 0 and i < n and S[i] == S[i - 1]: i += 1
                if i < 3 or S[i - 1] != S[i - 2] or S[i - 2] != S[i - 3]: return False
            return i == n and j == m
        return sum(check(S, W) for W in words)
```