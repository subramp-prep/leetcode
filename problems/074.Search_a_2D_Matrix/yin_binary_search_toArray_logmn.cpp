// Binary Search
// Time Complexity O(log(mn))
// Space Complexity O(1)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        // Corner cases
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        
        // Binary Search
        int m = matrix.size(), n = matrix[0].size(), i = 0, j = m * n- 1, mid;
        while (i <= j)
        {
            mid = (i + j) / 2;
            int val = matrix[mid/n][mid%n];
            if (target > val) i = mid + 1;
            else if (target < val) j = mid - 1;
            else return true;
        }
        return false;
    }
};