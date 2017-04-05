// Custom sort
// Time Complexity O(nlogn)
// Space Complexity O(1)
class Solution {
public:
    string largestNumber(vector<int>& nums)
    {
        // corner cases
        if (nums.empty()) return "0";
        
        // sort string
        auto cmp = [](const int& a, const int& b) { return to_string(a) + to_string(b) > to_string(b) + to_string(a); };
        sort(nums.begin(), nums.end(), cmp);
        
        // build result
        string res = "";
        for (int i = 0; i < nums.size(); ++i)
            res += to_string(nums[i]);
        return res[0] == '0' ? "0" : res;
    }
};