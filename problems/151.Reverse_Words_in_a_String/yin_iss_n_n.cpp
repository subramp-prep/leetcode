class Solution {
public:
    void reverseWords(string &s)
    {
        istringstream iss(s);
        string word;
        s = "";
        while (iss >> word)
            s = word + " " + s;
        s = s.substr(0, s.size() - 1);
    }
};