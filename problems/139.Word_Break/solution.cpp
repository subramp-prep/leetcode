#include <iostream>  //包含头文件iostream
#include <vector> //使用vector
#include <unordered_set>
using namespace std;  //使用命名空间std

class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        int len = (int)s.size();
        vector<bool> dp(len + 1, false);
        dp[0] = true;

        for(int i = 1; i <= len; i++) {
            for(int j = i - 1; j >= 0; j--) {
                if(dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[len];
    }


};

int main( ) {
    cout<<"This is a C++ program.\n";
    Solution s; 
    string str = "leetcode";
    unordered_set<string> dict; 
	dict.insert("leet");
	dict.insert("code");
    bool ret = s.wordBreak(str, dict);
    cout << ret << endl;            
    return 0;
}