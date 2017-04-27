// Brute Force
// Time Complexity O(n*sizeof(int))
// Space Complexity O(n)
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for (int i = 0; i <= num; ++i) {
            int x = i;
            while (x) {
                if (x % 2) ++res[i];
                x >>= 1;
            }
        }
        return res;
    }
};