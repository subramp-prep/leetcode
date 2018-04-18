#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    string mostCommonWord(string p, vector<string>& banned) {
        unordered_set<string> ban(banned.begin(), banned.end());
        unordered_map<string, int> count;
        paragraph += '.';
        int n = paragraph.size(), freq = 0;
        string ans, word;
        for (int i = 0; i < n; ++i) {
            if (isalpha(paragraph[i])) {
                word += tolower(paragraph[i]);
            }
            else if (!word.empty()) {
                if (ban.find(word) == ban.end() && ++count[word] > freq) {
                    freq = count[word];
                    ans = word;
                }
                word = "";
            }
        }
        return ans;
    }
};


int main() {
    Solution s;
    string paragraph = "hi hi ok.";
    vector<string> banned;
    cout << s.mostCommonWord(paragraph, banned) << endl;
    return 0;
}