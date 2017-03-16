// Simple search
// Time Complexity O(m+n)
// Space Complexity O(1)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        // Corner cases
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        
        int row = 0, colum = 0;
        
        // Determine row
        while (row < matrix.size())
            if (target >= matrix[row][0]) ++row;
            else break;
        if (row == 0) return false;
        --row;
        
        // Check if target in the row
        for (int i = 0; i < matrix[row].size(); ++i)
            if (matrix[row][i] == target) return true;
            
        return false;
    }
};