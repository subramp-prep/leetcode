// Binary Search Tree
// Time Complexity O(m+n)
// Space Complexity O(1)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        // Corner cases
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        
        // Search matrix
        int i = matrix.size() - 1, j = 0;
        while (i >= 0 && j < matrix[0].size())
        {
            if (target < matrix[i][j]) --i;
            else if (target > matrix[i][j]) ++j;
            else return true;
        }
        return false;
    }
};