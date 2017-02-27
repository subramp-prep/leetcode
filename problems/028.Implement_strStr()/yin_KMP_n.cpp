class Solution {
public:
    int strStr(string haystack, string needle)
    {
        // corner cases
        int lh = haystack.size(), ln = needle.size();
        if (lh < ln) return -1;
        if (ln == 0) return 0;
        
        // get "Partial match" table
        vector<int> T = getT(needle);
        
        // compare
        int i = 0, j = 0;
        while (i < lh && j < ln)
        {
            if (j == -1 || haystack[i] == needle[j])
            {
                ++i;
                ++j;
            }
            else
                j = T[j];
        }
        return (j == ln) ? i - ln : -1;
    }
    
    // get "Partial match" table
    vector<int> getT(string s)
    {
        int n = s.size(), j = -1, i = 0;
        vector<int> T(n, 0);
        T[0] = -1; // init
        
        while (i < n - 1)
        {
            if (j == -1 || s[i] == s[j])
                T[++i] = ++j;
            else
                j = T[j];
        }
        return T;
    }
};