class Solution {
public:
    int countSegments(string s)
    {
        istringstream iss(s);
        string seg;
        int res = 0;
        while (iss >> seg)
            ++res;
        return res;
    }
};