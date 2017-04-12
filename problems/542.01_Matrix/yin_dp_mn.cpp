// Dynamic programming
// Time Complexity O(mn)
// Space Complexity O(mn)
class Solution {
    int m, n;
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix)
    {
        m = matrix.size();
        n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, INT_MAX)); // init
        
        // scan forward
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                dpFill(dp, i, j, matrix[i][j]);
        
        // scan backward
        for (int i = m - 1; i >= 0; --i)
            for (int j = n - 1; j >= 0; --j)
                dpFill(dp, i, j, matrix[i][j]);
                
        return dp;
    }
    
    void dpFill(vector<vector<int>>& dp, int i, int j, int val)
    {
        //neighbours :    up      left     down     right
        int dirs[][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        if (val)
            for (auto dir : dirs) // fill with neighbours
            {
                int x = i + dir[0], y = j + dir[1];
                if (x >= 0 && y >= 0 && x < m && y < n && dp[x][y] != INT_MAX)
                    dp[i][j]= min(dp[i][j], dp[x][y] + 1);
            }
        else
            dp[i][j] = 0;
    }
};