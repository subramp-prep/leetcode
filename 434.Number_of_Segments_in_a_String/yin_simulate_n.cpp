class Solution {
public:
    int countSegments(string s)
    {
        s = s + " ";
        int i = 0, res = 0;
        char prec = ' ';
        while (i < s.size())
        {
            if (s[i] == ' ' && prec != ' ')
                ++res;
            prec = s[i];
            ++i;
        }
        return res;
    }
};