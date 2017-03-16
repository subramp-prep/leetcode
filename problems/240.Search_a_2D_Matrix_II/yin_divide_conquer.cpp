// Divide and Conquer
// Complexity : see readme.md
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        // Corner cases
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        
        // Divide and Conquer
        return helper(matrix, target, 0, 0, matrix.size() - 1, matrix[0].size() - 1);
    }
    
    // (x1, y1) up left point, (x2, y2) down right point
    bool helper(vector<vector<int>>& matrix, int target, int x1, int y1, int x2, int y2)
    {
        // end condition
        if(x2 < x1 || y2 < y1 || target < matrix[x1][y1] || target > matrix[x2][y2]) return false;
        
        // Binary Search for new end points
        int xm = (x1 + x2) / 2, ym = (y1 + y2) / 2, k = matrix[xm][ym];
        if (k == target) return true; // find target
        if (k < target)
            return helper(matrix, target, xm + 1, ym + 1, x2, y2) //down right bloc
                || helper(matrix, target, x1, ym + 1, xm, y2) // down left bloc
                || helper(matrix, target, xm + 1, y1, x2, ym); // up right bloc
        if (k > target)
            return helper(matrix, target, x1, y1, xm - 1, ym - 1) // up left bloc
                || helper(matrix, target, xm, y1, x2, ym - 1) // up right bloc
                || helper(matrix, target, x1, ym, xm - 1, y2); // down left bloc
    }
};