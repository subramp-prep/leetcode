// Two points
// Time complexity O(logn)
// Space complexity O(1)
class Solution {
public:
    bool isHappy(int n)
    {
        int slow = n, fast = n;
        while (true)
        {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
            if (slow == 1 || fast == 1) return true;
            if (slow == fast) return false;
        }
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