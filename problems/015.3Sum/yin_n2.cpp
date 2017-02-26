class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums)
    {
        vector<vector<int>> res;
        
        std::sort(nums.begin(), nums.end()); // sort
        
        for (int i = 0; i < nums.size() && nums[i] <= 0; ++i) // the smallest number <= 0
        {
            // fix a target of two sum to find
            int target = -nums[i];
            
            // interval
            int left = i + 1;
            int right = nums.size() - 1;
            
            // find two sums
			/// the key is to avoid duplicates
            while(left < right && nums[right] >= 0) // the biggest number >= 0
            {
                int sum = nums[left] + nums[right];
                if (sum > target)
                {
                    while (left < right && nums[--right] == nums[right + 1]); // avoid duplicates
                }
                else if (sum < target)
                {
                    while (left < right && nums[++left] == nums[left - 1]); // avoid duplicates
                }
                else //equal
                {
                    vector<int> triplet(3, 0);
					triplet[0] = nums[i];
					triplet[1] = nums[left];
					triplet[2] = nums[right];
					res.push_back(triplet);
                    while (left < right && nums[++left] == nums[left - 1]); // avoid duplicates
                    while (left < right && nums[--right] == nums[right + 1]); // avoid duplicates
                }
            }
            
            // avoid duplicates of i
            while (i < nums.size() - 1 && nums[i + 1] == nums[i]) 
                ++i;
        }
        return res;
    }
};