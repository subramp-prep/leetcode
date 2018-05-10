#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    string mostCommonWord(string p, vector<string>& banned) {
        unordered_set<string> ban(banned.begin(), banned.end());
        unordered_map<string, int> count;
        for (auto & c: p) c = isalpha(c) ? tolower(c) : ' ';
        istringstream iss(p);
        string w;
        pair<string, int> res ("", 0);
        while (iss >> w)
            if (ban.find(w) == ban.end() && ++count[w] > res.second)
                res = make_pair(w, count[w]);
        return res.first;
    }
};


int main() {
    Solution s;
    string paragraph = "abc abc  abcd the jeff";
    vector<string> banned;
    banned.push_back("abc");
    banned.push_back("abcd");
    banned.push_back("jeff");
    cout << s.mostCommonWord(paragraph, banned) << endl;
    return 0;
}