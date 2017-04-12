// Breath-first Search
// Time Complexity O(mn)
// Space Complexity O(mn)
class Solution {
    int m, n;
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix)
    {
        int m = matrix.size(), n = matrix[0].size();
        queue<pair<int, int>> que; // queue for positions of 0
        vector<vector<int>> res(m, vector<int>(n, INT_MAX));
        
        // init
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (matrix[i][j] == 0)
                {
                    res[i][j] = 0;
                    que.push(make_pair(i, j));
                }
                
        //neighbours :    up      left     down     right
        int dirs[][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        
        // bfs
        while (!que.empty())
        {
            pair<int, int> curr = que.front(); que.pop();
            for (auto dir : dirs) // fill with neighbours
            {
                int i = curr.first + dir[0], j = curr.second + dir[1];
                if (i < 0 || j < 0 || i >= m || j >= n || res[curr.first][curr.second] + 1 > res[i][j])
                    continue;
                res[i][j] = res[curr.first][curr.second] + 1;
                que.push(make_pair(i, j));
            }
        }
        
        return res;
    }
};