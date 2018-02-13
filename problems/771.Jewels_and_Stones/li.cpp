class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int res = 0;
        unordered_set<char> setJ;
        for (auto j : J) setJ.insert (j);
        for (auto s : S) if (setJ.find (s) != setJ.end ()) res++;
        return res;
    }
};



class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int res = 0;
        set<char> setJ(J.begin(), J.end());
        for (char s : S) if (setJ.count(s)) res++;
        return res;
    }
};



