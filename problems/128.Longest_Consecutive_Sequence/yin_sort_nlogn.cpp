class Solution {
public:
    int longestConsecutive(vector<int>& nums)
    {
        std::sort(nums.begin(), nums.end()); // sort
        
        int res = 0, len;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (i == 0) len = 0; // the first number
            else if (nums[i - 1] == nums[i]) continue; // handle repeated numbers
            else if (nums[i - 1] + 1 != nums[i]) { res = max(len, res); len = 0;}
            ++len;
        }
        
        res = max(len, res);
        return res;
    }
};