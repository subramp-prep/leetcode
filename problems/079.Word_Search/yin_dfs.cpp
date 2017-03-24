// Depth-first Search + Backtracking
// Time Complexity O(m*n*4^k) (k: length of word)
// Space Complexity O(mn)
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word)
    {
        // corner cases
        if (board.empty() || board[0].empty() || word.empty()) return false;
        int m = board.size(), n = board[0].size();
        if (m * n < word.size()) return false;
        
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (exist(board, word, i, j, 0)) // check
                    return true;
        
        return false;
    }
    
    // recursive
    bool exist(vector<vector<char>>& board, string word, int i, int j, int index)
    {
        if (index == word.size()) return true;
        int m = board.size(), n = board[0].size();
        if (i < 0 || j < 0 || i >= m || j >= n || word[index] != board[i][j]) return false;
        
        char temp = board[i][j];
        board[i][j] = '.'; // mark case as visited
        bool res = exist(board, word, i + 1, j, index + 1)
                || exist(board, word, i, j + 1, index + 1)
                || exist(board, word, i - 1, j, index + 1)
                || exist(board, word, i, j - 1, index + 1);
        board[i][j] = temp; // restore value
        return res;
    }
};