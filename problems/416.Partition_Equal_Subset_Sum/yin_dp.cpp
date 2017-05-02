// Dynamic Programming
// Time Complexity O(sum*n) < O(const*n)~O(n)
// Space Complexity O(sum) < O(const)~O(1)
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum & 1) return false;
        int target = sum / 2;
        
        // init dp
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        
		// update dp
        for (auto n : nums)
            for (int i = target; i >= n; --i)
                dp[i] = dp[i] || dp[i - n];
        
		// return
		return dp[target];
    }
};