// Brute force
// Time Complexity O(2^n)
// Space Complexity O(2^n)
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        return longestPalindromeSubseq(s, 0, s.size() - 1);
    }
    
    int longestPalindromeSubseq(const string& s, int i, int j) {
        if (i == j) return 1;	// odd "aaa"
        if (i > j) return 0;	// even "aa"
        if (s[i] == s[j]) {
            return 2 + longestPalindromeSubseq(s, i + 1, j - 1);
        }
        else {
            return max(longestPalindromeSubseq(s, i + 1, j), longestPalindromeSubseq(s, i, j - 1));
        }
    }
};