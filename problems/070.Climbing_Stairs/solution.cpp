#include <iostream>  //包含头文件iostream
using namespace std;  //使用命名空间std

class Solution {
public:
	int climbStairs(int n) {
		        int f1 = 2;
		        int f2 = 1;
		        if(n == 1) {
		            return f2;
		        } else if(n == 2) {
		            return f1;
		        }

		        int fn;
		        for(int i = 3; i <= n; i++) {
		            fn = f1 + f2;
		            f2 = f1;
		            f1 = fn;
		        }
		        return fn;
	}
};

int main( )
{
    cout<<"This is a C++ program.\n";
	Solution s;
	cout << s.climbStairs(5);
	cout << '\n';		
    return 0;
}