#include <iostream>  //包含头文件iostream
using namespace std;  //使用命名空间std

class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while (x) {
            int temp = ans * 10 + x % 10;
            if (temp / 10 != ans)
                return 0;
            ans = temp;
            x /= 10;
        }
        return ans;
    }
};

int main( )
{
    cout<<"This is a C++ program.\n";
	Solution s;
	cout<<s.reverse(15342364619);
			
    return 0;
}