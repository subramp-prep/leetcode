// Recursion
// Time Complexity O(m!n!)
// Space Complexity O(1)
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon)
    {
        return calculateHelper(dungeon, 0, 0);
    }
    
    // recursion
    int calculateHelper(vector<vector<int>>& dungeon, int i, int j)
    {
        int m = dungeon.size(), n = dungeon[0].size();
        
        if (i == m - 1 && j == n - 1) return max(1, 1 - dungeon[i][j]);
        if (i == m - 1 && j != n - 1) return max(1, calculateHelper(dungeon, i, j + 1) - dungeon[i][j]);
        if (i != m - 1 && j == n - 1) return max(1, calculateHelper(dungeon, i + 1, j) - dungeon[i][j]);
        return max(1, min(calculateHelper(dungeon, i + 1, j), calculateHelper(dungeon, i, j + 1)) - dungeon[i][j]);
    }
};