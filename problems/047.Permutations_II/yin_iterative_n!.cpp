// Iterative
// Time Complexity O(n*n!)
// Space Complexity O(n)
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums)
    {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res(1, vector<int>());
        for (int i = 0; i < nums.size(); ++i)
        {
            vector<vector<int>> temp(res);
            res.clear();
            for (int j = 0; j < temp.size(); ++j)
            {
                for (int k = 0; k <= temp[j].size(); ++k)
                {
                    if (k != 0 && temp[j][k - 1] == nums[i]) break;
                    vector<int> sub(temp[j]);
                    sub.insert(sub.begin() + k, nums[i]);
                    res.push_back(sub);
                }
            }
        }
        return res;
    }
};