class Solution {
public:
    int removeElement(vector<int>& nums, int val)
    {
        int shift = 0, n = nums.size();
        for (int i = 0; i < n; ++i)
        {
            if (nums[i] == val) ++shift;
            else nums[i - shift] = nums[i];
        }
        return n - shift;
    }
};