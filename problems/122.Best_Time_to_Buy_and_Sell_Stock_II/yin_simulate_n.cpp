// Simulate
// Time Complexity O(n)
// Space Complexity O(1)
class Solution {
public:
    int maxProfit(vector<int>& prices)
    {
        if (prices.empty()) return 0;
        int total = 0, i = 0;
        while (i < prices.size())
        {
            // find next min
            while(i < prices.size() - 1 && prices[i + 1] <= prices[i]) ++i;
            int min = i;
            
            // find next max
            while(i < prices.size() - 1 && prices[i + 1] >= prices[i]) ++i;
            total += (i < prices.size() ? prices[i++] - prices[min] : 0);
        }
        return total;
    }
};