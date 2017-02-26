// The number of stones is less than 1100 so pos will always be less than 2^11 (2048).
// Stone positions could be theoretically up to 2^31 
// but k is practically not possible to be that big for the parameter 
// as the steps must start from 0 and 1 and at the 1100th step the greatest valid k would be 1100. 
// So combining pos and k is safe here.
// <100ms
class Solution {
public:
    unordered_map<int, bool> dp;
    bool canCross(vector<int>& stones, int pos = 0, int k = 0) {
        int key = pos | k << 11;
    
        if (dp.count(key) > 0)
            return dp[key];
    
        for (int i = pos + 1; i < stones.size(); i++) {
            int gap = stones[i] - stones[pos];
            if (gap < k - 1)
                continue;
            if (gap > k + 1)
                return dp[key] = false;
            if (canCross(stones, i, gap))
                return dp[key] = true;
        }
    
        return dp[key] = (pos == stones.size() - 1);
    }
};