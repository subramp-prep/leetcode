// Hash Set
// Time complexity O(logn)
// Space complexity O(logn)
class Solution {
public:
    bool isHappy(int n)
    {
        unordered_set<int> set;
        while (true)
        {
            set.insert(n);
            n = getNext(n);
            if (n == 1) return true;
            if (set.find(n) != set.end()) return false;
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