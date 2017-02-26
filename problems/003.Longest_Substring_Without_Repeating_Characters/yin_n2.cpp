class Solution {
public:
    int lengthOfLongestSubstring(string s)
    {
        int res = 0;
        int currSize = 0;
        unordered_map<int, int> hash;
        int i = 0;
        
        while (i < s.size())
        {
            
            if (hash.find(s[i]) != hash.end())
            {
                // reset size
                res = max(res, currSize);
                currSize = 1;
                
                // reset hash table
                i = hash[s[i]] + 1;
                hash.clear();
            }
            else
            {
                hash[s[i]] = i;
                ++currSize;
            }
            
            hash[s[i]] = i;
            ++i;
        }
        
        res = max(res, currSize);
        
        return res;
    }
};