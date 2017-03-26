// Iterative
// Time Complexity O(2^n)
// Space Complexity O(n)
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums)
    {
        vector<vector<int>> res(1, vector<int>());
        sort(nums.begin(), nums.end());
        int size = 0, start = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            start = (i != 0 && nums[i] == nums[i - 1]) ? size : 0;
            size = res.size();
            for (int j = start; j < size; ++j)
            {
                vector<int> sub = res[j];
                sub.push_back(nums[i]);
                res.push_back(sub);
            }
        }
        return res;
    }
};