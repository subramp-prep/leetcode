// Hash Table
// Time Complexity O(n+m)
// Space Complexity O(n)
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2)
    {
        vector<int> res;
        unordered_set<int> set(nums1.begin(), nums1.end());
        for (auto n : nums2)
        {
            if (set.count(n))
            {
                res.push_back(n);
                set.erase(n);
            }
        }
        return res;
    }
};