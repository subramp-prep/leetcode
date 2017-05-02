class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        sort(nums.rbegin(), nums.rend());
        return !(sum & 1) && parHelper(nums, 0, sum / 2);
    }
    
    bool parHelper(vector<int>& nums, int i, int target) {
        // end conditions
        if(target == nums[i]) return true;
        if(target < nums[i]) return false;
        
        // recursion
        return parHelper(nums, i + 1, target - nums[i]) || parHelper(nums, i + 1, target);
    }
};