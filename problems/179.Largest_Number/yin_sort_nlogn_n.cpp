// Custom sort
// Time Complexity O(nlogn)
// Space Complexity O(n)
class Solution {
public:
    string largestNumber(vector<int>& nums)
    {
        // corner cases
        if (nums.empty()) return "0";
        
        // convert int to string
        vector<string> strs;
        for (int i = 0; i < nums.size(); ++i)
            strs.push_back(to_string(nums[i]));
        
        // sort string
        auto cmp = [](const string& a, const string& b) { return a + b > b + a; };
        sort(strs.begin(), strs.end(), cmp);
        
        // build result
        string res = "";
        for (int i = 0; i < strs.size(); ++i)
            res += strs[i];
        return res[0] == '0' ? "0" : res;
    }
};