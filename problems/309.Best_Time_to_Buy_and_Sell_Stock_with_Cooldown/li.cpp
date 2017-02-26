#include <iostream>  //包含头文件iostream
#include <vector> //使用vector
using namespace std;  //使用命名空间std

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n <= 1) return 0;
        vector<int> ret; //the maxProfit if no stock and no sell on ith day 
        vector<int> buy; //the maxProfit if sell on ith day 
        ret.resize(n);
        buy.resize(n);
        buy[0] = -1; // no possible to sell on the first day.
        ret[0] = 0;	 // no profit at first
        buy[1] = prices[1]>prices[0]? prices[1]-prices[0]:0; //maxProfit possible on the second day 
        ret[1] = 0; // no sell so no profit
        
        for(int i = 2; i < n; i++) {
            ret[i] = max(buy[i-1], ret[i-1]);
            if(prices[i]>prices[i-1]) {
                buy[i] = max(buy[i-1], ret[i-2]) + prices[i] - prices[i-1]; //2 plan to sell on ith day
            } else {
                buy[i] = buy[i-1] + prices[i] - prices[i-1]; //only one possible plan to sell on ith day
            }
        }
        for(int i = 0; i < n; i++) { //print the process
            cout << prices[i] << " " << ret[i] << " " << buy[i] << " " << endl;
        }
        return max(buy[n-1], ret[n-1]);
    }
	
	
};

int main( ) {
    cout<<"This is a C++ program.\n";
	Solution s;	
    int n[] = {6,1,3,2,4,7} ;//[1,2,3,0,2],[6,1,3,2,4,7]
    vector<int> prices(n, n + sizeof(n)/sizeof(int)) ;              //将数组n的前5个元素作为向量a的初值
	int ret = s.maxProfit(prices);
	cout << ret << endl;			
    return 0;
}