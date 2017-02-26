class Solution {
public:
    int strStr(string haystack, string needle)
    {
        // empty
        if (haystack.empty())
            if (needle.empty()) return 0;
            else return -1;

        int l = needle.size(), n = haystack.size();
        for (int i = 0; i + l <= n; ++i)
        {
            if (haystack.substr(i, l) == needle)
                return i;
        }
        return -1;
    }
};