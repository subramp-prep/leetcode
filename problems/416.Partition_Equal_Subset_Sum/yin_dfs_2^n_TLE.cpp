// Depth First Search
// Time Complexity O(2^n)
// Space Complexity O(2^n)
// Time Limit Exceeded : 89 / 104 test cases passed.
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        return !(sum & 1) && parHelper(nums, 0, sum / 2);
    }
    
    bool parHelper(vector<int>& nums, int start, int target) {
        // end conditions
        if (target < 0) return false;
        if (target == 0) return true;
        
        // recursion
        for (int i = start; i < nums.size(); ++i) 
            if (parHelper(nums, i + 1, target - nums[i]))
                return true;
        return false;
    }
};