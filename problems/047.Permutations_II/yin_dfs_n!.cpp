// Backtracking + Depth-first Search
// Time Complexity O(n!)
// Space Complexity O(n*n!)
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums)
    {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        permuteDfs(nums, 0, res);
        return res;
    }
    
    void permuteDfs(vector<int> nums, int start, vector<vector<int>>& res)
    {
        if (start == nums.size())
        {
            res.push_back(nums);
            return;
        }
        
        for (int i = start; i < nums.size(); ++i)
        {
            if (i != start && nums[i] == nums[start]) continue;
            swap(nums[start], nums[i]); // swap
            permuteDfs(nums, start + 1, res);
        }
    }
};