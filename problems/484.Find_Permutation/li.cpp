// Author:      Jianghan LI
// File:        li.py
// Create Date: 2017-01-21

class Solution {
public:
    vector<int> findPermutation(string s) {
    s = s.append("I");
    int countD = 0;
    vector<int> ret;
    for (int i = 0; i < s.size(); i++) {
      countD++;
      if (s[i] == 'I') {
        int retLen = ret.size();
        while (countD) ret.push_back(retLen + countD--);
      }
    }
    return ret;
  }
};

//同li.py
//为了在leetcode的一些vote
//谢谢大家支持