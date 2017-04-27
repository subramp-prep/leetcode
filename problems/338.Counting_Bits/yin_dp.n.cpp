// Dynamic programming
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for (int i = 1; i <= num; ++i)
            res[i] = res[i & (i - 1)] + 1;
        return res;
    }
};

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for (int i = 1; i <= num; ++i)
            res[i] = res[i >> 1] + (i & 1);
        return res;
    }
};

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for (int i = 1; i <= num; ++i)
            res[i] = res[i / 2] + (i % 2);
        return res;
    }
};