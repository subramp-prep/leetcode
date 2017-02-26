// Author:      Jianghan LI
// File:        li.py
// Create Date: 2017-01-21

class Solution {
public:
  vector<int> findPermutation(string s) {
    vector<int> ret;
    for (int i = 0; i <= s.size(); ++i)
      if (i == s.size() || s[i] == 'I')
        for (int j = i + 1, lenTmp = ret.size(); j > lenTmp; --j)
          ret.push_back(j);
    return ret;
  }
};


//C++ simple solution in 72ms and 9 lines
//同li.py
//为了在leetcode的一些vote
//谢谢大家支持
//https://discuss.leetcode.com/topic/76230/c-simple-solution-in-75ms-and-11-lines