// Simulate
// Time Complexity O(n2)
// Space Complexity O(n)
class Solution {
public:
    string removeKdigits(string num, int k)
    {
        int n = num.size();
        if (n <= k) return "0"; // all digits removed
        
        string res = "";
        for (int i = 0, j = k; j < n; ++j)
        {
            int min = 10;
            for (int h = i; h <= j; ++h)
            {
                int digit = num[h] - '0';
                if (digit < min)
                {
                    min = digit;
                    i = h + 1;
                }
            }
            if (!res.empty() || min > 0) res += to_string(min);
        }
        return res.empty() ? "0" : res;
    }
};