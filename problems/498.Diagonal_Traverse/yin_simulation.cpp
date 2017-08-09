// Simulation
// Time Complexity O(mn)
// Space Complexity O(mn)
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix)
    {
        vector<int> res;
        if (!matrix.size()) return res;
        
        int i = 0, j = 0, m = matrix.size(), n = matrix[0].size(), step = 1;
        while(i < m - 1 || j < n - 1)
        {
            res.push_back(matrix[i][j]);
            i -= step; j += step;
            if (i < 0 || j < 0 || i >= m || j >= n)
            {
                step = -step; // Change direction
                if (i >= m) {i = m - 1; j += 2;};
                if (j >= n) {j = n - 1; i += 2;};
                if (i < 0) i = 0;
                if (j < 0) j = 0;
            }
        }
        res.push_back(matrix[i][j]);
        return res;
    }
};