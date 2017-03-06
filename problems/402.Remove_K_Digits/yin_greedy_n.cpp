// Greedy Algo
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    string removeKdigits(string num, int k)
    {
        int n = num.size(), top = 0;
        if (n <= k) return "0"; // all digits removed
        
        string res(n, 0);
        for (int i = 0, j = k; i < n; ++i)
        {
            // compare the digit to be added with last digits added
            while (top > 0 && res[top - 1] > num[i] && j > 0)
            {
                --top; --j; // remove digit larger than current one
            }
            res[top++] = num[i]; // add this digit
        }
        
        // find the index of first non-zero digit
        int idx = 0;
        while (idx < res.size() && res[idx] == '0') idx++;
        res = res.substr(idx, n - k - idx);
        return (idx == n - k) ? "0" : res; //! we can't use res.empty() to judge here
    }
};