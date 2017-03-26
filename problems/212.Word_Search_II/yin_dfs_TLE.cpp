class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words)
    {
        words.erase(unique(words.begin(), words.end()), words.end()); // remove duplicates
        vector<string> res;
        for (int i = 0; i < words.size(); ++i)
            if (findWord(board, words[i]))
                res.push_back(words[i]);
        return res;
    }
    
    bool findWord(vector<vector<char>>& board, string word)
    {
        // corner cases
        if (board.empty() || board[0].empty() || word.empty()) return false;
        int m = board.size(), n = board[0].size();
        if (m * n < word.size()) return false;
        
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (findWord(board, word, i, j, 0)) // check
                    return true;
        
        return false;
    }
    
    // recursive
    bool findWord(vector<vector<char>>& board, string word, int i, int j, int index)
    {
        if (index == word.size()) return true;
        int m = board.size(), n = board[0].size();
        if (i < 0 || j < 0 || i >= m || j >= n || word[index] != board[i][j]) return false;
        
        char temp = board[i][j];
        board[i][j] = '.'; // mark case as visited
        bool res = findWord(board, word, i + 1, j, index + 1)
                || findWord(board, word, i, j + 1, index + 1)
                || findWord(board, word, i - 1, j, index + 1)
                || findWord(board, word, i, j - 1, index + 1);
        board[i][j] = temp; // restore value
        return res;
    }
};