class Solution {
public:
    int longestConsecutive(vector<int>& nums)
    {
        unordered_set<int> set;
        
        // Stock nums in set
        for (int i = 0; i < nums.size(); ++i)
        {
            if (set.find(nums[i]) == set.end())
                set.insert(nums[i]);
        }
        
        // 
        int num, len, res = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            // determine the smallest number
            if (set.find(nums[i] - 1) == set.end())
            {
                num = nums[i];
                len = 1;
                // get consecutive numbers 
                while (set.find(++num) != set.end())
                {
                    ++len;
                }
                // update result
                res = max(len, res);
            }
        }
        return res;
    }
};