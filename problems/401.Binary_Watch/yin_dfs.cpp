// Backtracking + Depth-first Search
// Time Complexity O(n*2^n)
class Solution {
public:
    vector<string> readBinaryWatch(int num)
    {
        vector<string> res;
        for (int i = 0; i <= min(num, 3); ++i)
        {
            vector<int> hours = genDigits({1, 2, 4, 8}, i);
            vector<int> minutes = genDigits({1, 2, 4, 8, 16, 32}, num - i);
            for (int j = 0; j < hours.size(); ++j)
                for (int k = 0; k < minutes.size(); ++k)
                    if (hours[j] < 12 && minutes[k] < 60)
                        res.push_back(to_string(hours[j]) + (minutes[k] < 10 ? ":0" : ":") + to_string(minutes[k]));
        }
        return res;
    }
    
    vector<int> genDigits(const vector<int>& nums, int nb)
    {
        vector<int> res;
        genDigitsHelper(nums, 0, nb, 0, res);
        return res;
    }
    
    void genDigitsHelper(const vector<int>& nums, int start, int nb, int sum, vector<int>& res)
    {
        if (nb == 0) { res.push_back(sum); return; }
		if (start + nb > nums.size()) return;
        for (int i = start; i < nums.size(); ++i)
            genDigitsHelper(nums, i + 1, nb - 1, sum + nums[i], res);
    }
};