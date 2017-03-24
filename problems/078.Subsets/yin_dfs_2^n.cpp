// Backtracking
// Time Complexity O(2^n)
// Space Complexity O(2^n)
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums)
    {
        vector<vector<int>> res;
        vector<int> sub;
        addSubset(nums, 0, sub, res);
        return res;
    }
    
    void addSubset(vector<int>& nums, int k, vector<int>& sub, vector<vector<int>>& res)
    {
        res.push_back(sub);
        for (int i = k; i < nums.size(); ++i)
        {
            sub.push_back(nums[i]);
            addSubset(nums, i + 1, sub, res);
            sub.pop_back();
        }
    }
};