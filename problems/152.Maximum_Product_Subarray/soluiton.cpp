/*
maxDP[i + 1] = max(maxDP[i] * A[i + 1], A[i + 1], minDP[i] * A[i + 1])
minDP[i + 1] = min(minDP[i] * A[i + 1], A[i + 1], maxDP[i] * A[i + 1]
dp[i + 1] = max(dp[i], maxDP[i + 1])
这里，我们还需要注意元素为0的情况，如果A[i]为0，那么maxDP和minDP都为0，我们需要从A[i + 1]重新开始。
*/
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        if(n == 0){
            return 0;
        } else if (n == 1) {
            return nums[0];
        }

        int p = nums[0];
        int maxP = nums[0];
        int minP = nums[0];
        for(int i = 1; i < n; i++) {
            int t = maxP;
            maxP = max(max(maxP * nums[i], nums[i]), minP * nums[i]);
            minP = min(min(t * nums[i], nums[i]), minP * nums[i]);
            p = max(maxP, p);
        }

        return p;
    }
};