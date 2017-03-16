// Binary Search
// Time Complexity O(log(m)+log(n))
// Space Complexity O(1)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        // Corner cases
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        
        // Determine row
        int i = 0, j = matrix.size() - 1, mid, row;
        while (i <= j)
        {
            mid = (i + j) / 2;
            if (target > matrix[mid][0]) i = mid + 1;
            else if (target < matrix[mid][0]) j = mid - 1;
            else return true;
        }
        if (j < 0) return false;
        row = j;
        
        // Check in the row
        i = 0;
        j = matrix[row].size() - 1; 
        while (i <= j)
        {
            mid = (i + j) / 2;
            if (target > matrix[row][mid]) i = mid + 1;
            else if (target < matrix[row][mid]) j = mid - 1;
            else return true;
        }
            
        return false;
    }
};