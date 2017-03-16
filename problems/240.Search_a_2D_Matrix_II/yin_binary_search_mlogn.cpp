// Binary Search row by row
// Time Complexity O(mlogn)
// Space Complexity O(1)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        // Corner cases
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        
        // Binary search row by row
        int n = matrix[0].size();
        for (int row = 0; row < matrix.size(); ++row)
        {
            if (target < matrix[row][0]) continue;
            if (target > matrix[row][n - 1]) continue;
            int i = 0, j = n - 1, mid;
            while (i <= j)
            {
                mid = (i + j) / 2;
                if (target > matrix[row][mid]) i = mid + 1;
                else if (target < matrix[row][mid]) j = mid - 1;
                else return true;
            }
        }
        return false;
    }
};