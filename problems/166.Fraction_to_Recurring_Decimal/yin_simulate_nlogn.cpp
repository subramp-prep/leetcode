// Simulate
// Time Complexity O(nlogn)
// Space Complexity O(n)
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator)
    {
        long long n = numerator, d = denominator; // prevent overflow
        string res = "";
        
        // sign of result
        if ((n < 0 && d > 0) || (n > 0 && d < 0)) res += '-';
        n = max(n, -n); d = max(d, -d);
        
        // integer part
        res += to_string(n / d);
        n = n % d;
        if (n == 0) return res;
        
        // decimal part
        res += ".";
        n *= 10;
        unordered_map<long, long> mp; 
        while (n) {
            int num = n / d;
            if (mp.find(n) != mp.end()) { 
                res.insert(mp[n], 1, '(');
                res += ')';
                break;
            }
            mp[n] = res.size();
            res += to_string(num);
            n = (n % d) * 10;
        }
        return res;
    }
};