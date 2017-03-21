// Binary Search
// Time Complexity O(mn)
// Space Complexity O(mn)
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>> &dungeon)
    {
        int i = 1, j = INT_MAX;
        while (i < j)
        {
            int mid = (j - i) / 2 + i; // don't use (i + j) / 2, overflow
            if (check(dungeon, mid)) // true => this initial hp is big enough
                j = mid;
            else // false => this initial hp is too small
                i = mid + 1;
        }
        return i;
    }
    
    // check function will go through the dungeon with hp input
    // check if he can survive
    int check(vector<vector<int>> &dungeon, int hp)
    {
        int m = dungeon.size(), n = dungeon[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0)); // dp
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
            {
                if (i == 0 && j == 0) // Init
                    dp[i][j] = hp + dungeon[i][j];
                else if (i == 0 && j != 0) // First row
                    dp[i][j] = (dp[i][j - 1] > 0 ? dp[i][j - 1] + dungeon[i][j] : 0);
                else if (i != 0 && j == 0) // First colum
                    dp[i][j] = (dp[i - 1][j] > 0 ? dp[i - 1][j] + dungeon[i][j] : 0);
                else if (dp[i][j - 1] > 0 || dp[i - 1][j] > 0)
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + dungeon[i][j];
                else continue; // no possible way leading to this bloc, leave dp to 0
            }
        return dp[m - 1][n - 1] > 0;
    }
};