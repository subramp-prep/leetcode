class Solution {
public:
    int kthGrammar(int N, int K) {
        int res = 0;
        while (K > 1) {
            K = K % 2 == 1 ? K + 1 : K / 2;
            res ^= 1;
        }
        return res;
    }
};