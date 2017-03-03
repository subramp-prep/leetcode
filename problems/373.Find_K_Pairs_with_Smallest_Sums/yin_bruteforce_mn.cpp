// Brute force
// Time Complexity O(mn)
// Space Complexity O(mn)
class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k)
    {
        int n1 = nums1.size(), n2 = nums2.size();
        vector<pair<int, int>> res;
        if (n1 == 0 || n2 == 0 || k == 0) return res; // empty input
        
        // produce all pairs
        for (int i = 0; i < n1; ++i)
            for (int j = 0; j < n2; ++j)
                res.push_back(make_pair(nums1[i], nums2[j]));
        
        // sort them by sum
        auto cmp = [](pair<int, int> p1, pair<int, int> p2) { return p1.first + p1.second < p2.first + p2.second; }; // custom compare
        sort(res.begin(), res.end(), cmp);
        
        //return first k values
		if (res.size() > k) res.erase(res.begin() + k, res.end());
        return res;
    }
};