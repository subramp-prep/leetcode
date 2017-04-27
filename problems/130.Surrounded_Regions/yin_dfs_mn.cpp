// Depth-first Search
// Time Complexity O(mn)
// Space Complexity O(mn)
class Solution {
public:
    void solve(vector<vector<char>>& board)
    {
        if (board.size() == 0 || board[0].size() == 0) return;
        int m = board.size(), n = board[0].size();
        
        // Spread from borders
        for (int i = 0; i < m; ++i)
        {
            check(board, i, 0);
            if (n > 1) check(board, i, n - 1);
        }
        for (int j = 0; j < n; ++j)
        {
            check(board, 0, j);
            if (m > 1) check(board, m - 1, j);
        }
        
        // Convert results: '*'->'O', 'O'->'X'
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                switch (board[i][j])
                {
                    case '*': board[i][j] = 'O'; break;
                    case 'O': board[i][j] = 'X'; break;
                    default: break;
                }
    }
    
    void check(vector<vector<char>>& board, int i, int j)
    {
        if (board[i][j] != 'O') return;
        int m = board.size(), n = board[0].size();
        board[i][j] = '*';
        if (i > 1) check(board, i - 1, j);
        if (j > 1) check(board, i, j - 1);
        if (i < m - 1) check(board, i + 1, j);
        if (j < n - 1) check(board, i, j + 1);
    }
};