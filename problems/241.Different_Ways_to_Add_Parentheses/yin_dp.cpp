// Dynamic Programming + extract numbers and operators
// Time Complexity O(Cat(n))
// Space Complexity O(n^2*Cat(n))
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        // extract all numbers and operators
        vector<int> nums;
        vector<char> oprs;
        int num = 0;
        char opr = ' ';
        istringstream ss(input + "+");
        while(ss >> num && ss >> opr) {
           nums.push_back(num);
           oprs.push_back(opr);
        }
        
        // init dp
        int n = nums.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>()));
        // update dp
        for (int j = 0; j < n; ++j)
            for (int i = j; i >= 0; --i) {
                if (i == j) { dp[i][j].push_back(nums[i]); continue; }
                for (int k = i; k < j; ++k) {
                    for (auto n1 : dp[i][k]) 
                        for (auto n2 : dp[k + 1][j]) {
                            int val = 0;
                            switch(oprs[k]) {
                                case '+': val = n1 + n2; break;
                                case '-': val = n1 - n2; break;
                                case '*': val = n1 * n2; break;
                            }
                        dp[i][j].push_back(val);
                    }
                }
        }
        // return
        return dp[0][n - 1];
    }
};