/*
区别于自顶向下，另一种更简单的做法就是自底向上了。dp方程为

dp[m][n] = min(dp[m + 1][n], dp[m + 1][n + 1]) + triangle[m][n]

我们仍然可以使用一位数组滚动计算。

代码如下
*/
class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
        if(triangle.empty()) {
            return 0;
        }
        int row = triangle.size();
        vector<int> dp;
        dp.resize(row);
        //用最底层的数据初始化
        for(int i = 0; i < dp.size(); i++) {
            dp[i] = triangle[row-1][i];
        }

        for(int i = row - 2; i >= 0; i--) {
            for(int j = 0; j <= i; j++) {
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1]);
            }
        }
        return dp[0];
    }
};