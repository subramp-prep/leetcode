// Brute Force
// Time Complexity O(n^2)
// Space Complexity O(n)
// Time Limit Exceeded: 16 / 16 test cases passed
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                if (nums[j] < nums[i])
                    ++res[i];
        return res;
    }
};