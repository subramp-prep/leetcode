// Dynamic Programming
// Time Complexity O(mn)
// Space Complexity O(mn)
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon)
    {
        int m = dungeon.size(), n = dungeon[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Update dp
        for (int i = m - 1; i >= 0; --i)
            for (int j = n - 1; j >= 0; --j)
                if (i == m - 1 && j == n - 1) // Init
                    dp[i][j] = max(1, 1 - dungeon[i][j]);
                else if (i == m - 1 && j != n - 1) // Last row
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j]);
                else if (i != m - 1 && j == n - 1) // Last colum
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j]);
                else
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);
        
        // return
        return dp[0][0];
    }
};