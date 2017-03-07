// Under 100
// Time complexity O(logn)
// Space complexity O(1)
class Solution {
public:
    bool isHappy(int n)
    {
        int nums[20] = {1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100};
        while (n > 100)
            n = getNext(n);
        
        for (int i = 0; i < 20; ++i)
            if (nums[i] == n)
                return true;
        return false;
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