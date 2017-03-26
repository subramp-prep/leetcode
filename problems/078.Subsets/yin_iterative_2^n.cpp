// Iterative
// Time Complexity O(2^n)
// Space Complexity O(n)
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums)
    {
        vector<vector<int>> res(1, vector<int>());
        for (int i = 0; i < nums.size(); ++i)
        {
            int size = res.size();
            for (int j = 0; j < size; ++j)
            {
                vector<int> sub = res[j];
                sub.push_back(nums[i]);
                res.push_back(sub);
            }
        }
        return res;
    }
};