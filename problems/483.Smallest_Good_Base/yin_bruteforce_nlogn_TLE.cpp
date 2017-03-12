// Brute Force
// Time Complexity O(nlogn)
// Space Complexity O(1)
class Solution {
public:
    string smallestGoodBase(string n)
    {
        unsigned long long val = stoull(n);
        for (unsigned long long k = 2; k < val; ++k)
            if (validate(val, k))
                return to_string(k);
        return NULL;
    }
    
    bool validate(unsigned long long val, unsigned long long k)
    {
        while (val > k)
        {
            if (val % k != 1) return false; // make sure every digit is 1
            val /= k;
        }
        return val == 1; // last digit is 1
    }
};