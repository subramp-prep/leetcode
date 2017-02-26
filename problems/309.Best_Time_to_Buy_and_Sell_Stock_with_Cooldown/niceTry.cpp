/*不错的思路，考虑到了很多情况。每天有三种情况，
buy＝0 是可买，buy＝1当天卖出并计算差价，buy＝2是cooldown的状态。
然而此算法不是动态编程；没有保存历史值和次优解，对于有些次优解逆袭特殊情况无法得到最优解。
Input:
	[8,6,4,3,3,2,3,5,8,3,8,2,6]
Output:
	8
Expected:
	10
Stdout:
	price ret buy
	6 0 0
	4 0 0
	3 0 0
	3 0 0
	2 0 0
	3 1 1
	5 3 1
	8 6 1
	3 6 2
	8 8 1
	2 8 2
	6 8 0
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ret = 0;
        int buy = 0;
        for(int i = 1; i < prices.size(); i++) {
            if(buy == 0 && prices[i]>prices[i-1]) {
                ret += prices[i] - prices[i-1];
                buy = 1;
            } else if (buy == 1 && prices[i]>=prices[i-1]) {
                ret += prices[i] - prices[i-1];
            } else if (buy == 1 && prices[i]<prices[i-1]) {
                buy = 2;
            } else if (buy == 2 && prices[i]>prices[i-1]) {
                if(prices[i-1] > prices[i-3] && prices[i] > prices[i-2]) {
                    ret += prices[i]-prices[i-2];
                    buy = 1;
                } else if(prices[i-1] <= prices[i-3] && prices[i-2]-prices[i-3] < prices[i]-prices[i-1]) {
                    ret += prices[i]-prices[i-1]-prices[i-2]+prices[i-3];
                    buy = 1;
                } else {
                    buy = 0;
                } 
            } else if (buy == 2) {
                buy = 0;
            } else {
                
            }
            cout<<prices[i]<<" "<<ret<<" "<<buy<<endl;
        }
        return ret;
    }
};