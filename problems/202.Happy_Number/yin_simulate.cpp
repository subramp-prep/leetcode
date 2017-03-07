// Simulate
// Time complexity O(logn)
// Space complexity O(1)
class Solution {
public:
    bool isHappy(int n)
    {
        while (n > 6)
            n = getNext(n);
        return n == 1;
    }
    
    int getNext(int n)
    {
        int res = 0;
        while (n > 0)
        {
            res += (n % 10) * (n % 10);
            n /= 10;
        }
        return res;
    }
};