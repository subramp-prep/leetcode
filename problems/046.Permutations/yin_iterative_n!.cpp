// Iterative
// Time Complexity O(n!)
// Space Complexity O(n)
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums)
    {
        vector<vector<int>> res(1, nums);
        for (int i = 0; i < nums.size(); ++i)
        {
            int size = res.size();
            for (int j = 0; j < size; ++j)
            {
                for (int k = i + 1; k < res[j].size(); ++k)
                {
                    vector<int> temp(res[j]);
                    swap(temp[i], temp[k]);
                    res.push_back(temp);
                }
            }
        }
        return res;
    }
};