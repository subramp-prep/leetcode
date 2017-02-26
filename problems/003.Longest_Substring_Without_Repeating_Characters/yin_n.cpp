class Solution {
public:
    int lengthOfLongestSubstring(string s)
    {
        int n = s.size(), res = 0;
        unordered_map<char, int> hash; // current index of character
        
        // i : index of left character
        // j : index of right character
        for (int i = 0, j = 0; j < n; j++) {
            // if right character occurs more than once
            if (hash.find(s[j]) != hash.end())
            {
                // change left character position to the next charachter of last occurence
                // add a comparison here to avoid error for cases like "abba"
                i = max(i, hash[s[j]] + 1);
            }
            
            // update result
            res = max(res, j - i + 1);
            
            // add index
            hash[s[j]] = j;
        }
        return res;
    }
};