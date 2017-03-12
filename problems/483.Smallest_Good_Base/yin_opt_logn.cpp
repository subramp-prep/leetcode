// Optimized Brute Force
// Time Complexity O(logn)
// Space Complexity O(1)
class Solution {
public:
    string smallestGoodBase(string n)
    {
        unsigned long long val = stoull(n);
        int maxdigits = ceil((long double)log(val) / (long double)log(2)); // min base is 2 => max digit number is log(val, 2)
        for (int i = maxdigits; i > 2; --i) // at least 2 digits when k = val - 1
        {
            int k = floor(pow((long double)(val), 1.0 / (i - 1))); // k <= i - 1 root square of val
            if (k == 1) continue;
            unsigned long long sum = (pow((long double)k, (long double)i) - 1) / (long double)(k - 1); // geometric sequence sum formulae
            if (sum == val)
                return to_string(k);
        }
        return to_string(val - 1);
    }
};