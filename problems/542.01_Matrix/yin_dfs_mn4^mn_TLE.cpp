// Depth-first Search
// Time Complexity O(mn*4^(mn))
// Space Complexity O(4^(mn))
// Time Limit Exceeded (29/48 test cases passed)
class Solution {
    int n, m;
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix)
    {
        m = matrix.size();
        n = matrix[0].size();
        vector<vector<int>> res(m, vector<int>(n, -1));
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (matrix[i][j] == 0)
                    dfsFill(res, i, j, 0);
        return res;
    }
    
    void dfsFill(vector<vector<int>>& res, int i, int j, int d)
    {
        // end conditions
        if (i < 0 || j < 0 || i >= m || j >= n || (res[i][j] >= 0 && res[i][j] <= d))
            return;
        
        // fill
        res[i][j] = d;
        dfsFill(res, i - 1, j, d + 1);
        dfsFill(res, i, j - 1, d + 1);
        dfsFill(res, i + 1, j, d + 1);
        dfsFill(res, i, j + 1, d + 1);
    }
};