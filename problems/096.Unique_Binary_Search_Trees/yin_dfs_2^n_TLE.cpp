// Depth First Search
// Time Complexity O(2^n)
// Space Complexity O(2^n)
// TLE (12/19 test cases passed)
class Solution {
public:
    int numTrees(int n) {
        if (n <= 1) return 1;
        int res = 0;
        for (int i = 1; i <= n; ++i)
            res += numTrees(i - 1) * numTrees(n - i);
        return res;
    }
};