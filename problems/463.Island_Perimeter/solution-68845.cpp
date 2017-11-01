//Edited by LI
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int neighbor = 0, island = 0;
        for (int i = 0; i < grid.size(); ++i)
            for (int j = 0; j < grid[i].size(); ++j)
                if (grid[i][j] == 1) {
                    ++island;
                    if (i && grid[i - 1][j]) ++neighbor;
                    if (j && grid[i][j - 1]) ++neighbor;
                }
        return island * 4 - neighbor * 2;
    }
};


//Edited by LI
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int res = 0;
        for (int i = 0; i < grid.size(); ++i)
            for (int j = 0; j < grid[i].size(); ++j)
                if (grid[i][j] == 1) {
                    ++++res;
                    if (i && grid[i - 1][j]) --res;
                    if (j && grid[i][j - 1]) --res;
                }
        return res * 2;
    }
};

