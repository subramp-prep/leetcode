// Bit Manipulation
// Time Complexity O(n*2^n)
// Space Complexity O(n)
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums)
    {
        int n = pow(2, nums.size());
		vector<vector<int>> res(n, vector<int>());
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < nums.size(); ++j)
				if ((i >> j) & 1)
					res[i].push_back(nums[j]);
		return res;
    }
};