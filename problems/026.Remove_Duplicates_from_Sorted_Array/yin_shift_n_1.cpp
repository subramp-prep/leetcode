class Solution {
public:
    int removeDuplicates(vector<int>& nums)
    {
        int shift = 0, n = nums.size();
        for (int i = 1; i < n; ++i)
        {
            if (nums[i] == nums[i - 1]) ++shift; // duplicated value, ++shift
            else nums[i - shift] = nums[i]; // not duplicated value, put it in the right pos
        }
        return n - shift;
    }
};