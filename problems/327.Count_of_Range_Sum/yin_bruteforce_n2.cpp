// Brute Force
// Time Complexity O(n^2)
// Space Complexity O(1)
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size(), res = 0;
        for (int i = 0; i < n; ++i) {
            long long sum = 0;
            for (int j = i; j < n; ++j) {
                sum += nums[j];
                if (sum >= lower && sum <= upper)
                    ++res;
            }
        }
        return res;
    }
};