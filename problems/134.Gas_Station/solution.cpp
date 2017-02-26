//134. Gas Station
#include <iostream>  //包含头文件iostream
#include <vector> //使用vector
using namespace std;  //使用命名空间std

class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
		int sum = 0;
        int total = 0;
        int k = 0;
        for(int i = 0; i < (int)gas.size(); i++) {
            sum += gas[i] - cost[i];
            //小于0就只可能在i + 1或者之后了
            if(sum < 0) {
                k = i + 1;
                sum = 0;
            }
            total += gas[i] - cost[i];
        }

        if(total < 0) {
            return -1;
        } else {
            return k;
        }
    }
    int mySolution(vector<int> &gas, vector<int> &cost) {
		int sum = 0;
		int min = 0;
		int res = -1;
        for(int i = 0; i < (int)gas.size(); i++) {
			sum += gas[i] - cost[i];
			if (sum < min){
				min = sum;
				res = i;
			}
        }
        if(sum < 0) {
            return -1;
        } else {
            return (res+1)%(int)gas.size();
        }
    }
};

int main( )
{
    cout<<"This is a C++ program.\n";
	Solution s;
	int n = 7;
	int gasArray[7] = {2,0,1,2,3,4,0};  
	vector<int> gas(gasArray, gasArray + n); 
	int costArray[7] = {0,1,0,0,0,0,11};  
	vector<int> cost(costArray, costArray + n);
	cout << s.canCompleteCircuit(gas, cost);
	cout << '\n';
	cout << s.mySolution(gas, cost);			
    return 0;
}