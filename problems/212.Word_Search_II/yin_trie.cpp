// Trie
// Time Complexity O(m*n*26^k)
// Space Complexity O(mn)
class Solution {
public:

    // Class Trie Node
    class TrieNode
    {
        public:
            vector<TrieNode *> next = vector<TrieNode *>(26, nullptr);
            string word = "";
            
            // destructor
            ~TrieNode()
            {
                for (int i = 0; i < 26; ++i)
                    if (next[i] != nullptr) { delete next[i]; next[i] = nullptr; }
            }
    };
    
    // Class Trie
    class Trie
    {
        private:
            TrieNode *root;
            
            // add word
            void addWord(string word)
            {
                TrieNode *p = root;
                for (int i = 0; i < word.size(); ++i)
                {
                    int idx = word[i] - 'a';
                    if (p->next[idx] == nullptr) p->next[idx] = new TrieNode();
                    p = p->next[idx];
                }
                p->word = word;
            }
            
        public:
            // getter
            TrieNode *getRoot() const { return root; }
            
            // constructor
            Trie(vector<string>& words)
            {
                root = new TrieNode();
                for(int i = 0; i < words.size(); ++i)
                    addWord(words[i]);
            }
            
            // destructor
            ~Trie()
            {
                delete root;
                root = nullptr;
            }
    };
    
    // solution
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words)
    {
        vector<string> res;
        Trie* trie = new Trie(words);
        TrieNode* root = trie->getRoot();
        for (int i = 0; i < board.size(); ++i)
            for (int j = 0; j < board[0].size(); ++j)
                findDfs(board, i, j, root, res);
        delete root;
        return res;
    }
    
    // dfs
    void findDfs(vector<vector<char>>& board, int i, int j, TrieNode *p, vector<string>& res)
    {
        int m = board.size(), n = board[0].size();
        if (i < 0 || j < 0 || i >= m || j >= n || board[i][j] == '#' || p == nullptr) return;
        char c = board[i][j];
        int idx = c - 'a';
        p = p->next[idx];
        if (p == nullptr) return;
        if (p->word != "")
        {
            res.push_back(p->word);
            p->word = ""; // avoid duplicate
        }
        
        board[i][j] = '#';
        findDfs(board, i - 1, j, p, res);
        findDfs(board, i + 1, j, p, res);
        findDfs(board, i, j - 1, p, res);
        findDfs(board, i, j + 1, p, res);
        board[i][j] = c;
    }
};