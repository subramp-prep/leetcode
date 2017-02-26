#include <iostream>  //包含头文件iostream
#include <vector> //使用vector
using namespace std;  //使用命名空间std

class Solution {
public:
    int candy(vector<int>& ratings) {
		vector<int> candys;
		//首先每人发一颗糖
		candys.resize(ratings.size(), 1);
		//这个循环保证了右边高级别的孩子一定比左边的孩子糖果数量多
		for(int i = 1; i < (int)ratings.size(); i++) {
			if(ratings[i - 1] < ratings[i]) {
		    	candys[i] = candys[i - 1] + 1;
		    }
		}

		//这个循环保证了左边高级别的孩子一定比右边的孩子糖果数量多
        for(int i = (int)ratings.size() - 2; i >= 0; i--) {
			if(ratings[i] > ratings[i + 1] && candys[i] <= candys[i + 1]) {
				candys[i] = candys[i + 1] + 1;
			}
		}
		int n = 0;
        for(int i = 0; i < (int)candys.size(); i++) {
            n += candys[i];
        }
        return n;
    }

    int candy2(vector<int>& ratings) {
		vector<int> candys;
		int nb = (int)ratings.size();
		//首先每人发一颗糖
		candys.resize(nb, 1);
		//这个循环保证了右边高级别的孩子一定比左边的孩子糖果数量多
		for(int i = 1; i < nb; i++) {
			if(ratings[i - 1] < ratings[i]) {
		    	candys[i] = candys[i - 1] + 1;
		    }
		}

		//这个循环保证了左边高级别的孩子一定比右边的孩子糖果数量多
        for(int i = nb - 2; i >= 0; i--) {
			if(ratings[i] > ratings[i + 1] && candys[i] <= candys[i + 1]) {
				candys[i] = candys[i + 1] + 1;
			}
		}
		int n = 0;
        for(int i = 0; i < nb; i++) {
            n += candys[i];
        }
        return n;
    }

    int myWrongSolution(vector<int>& ratings) {
		if ((int)ratings.size() == 0) return 0;
		int n = 1;
		int current = 1;
        for(int i = 1; i < (int)ratings.size(); i++) {
			if (ratings[i-1] < ratings[i]) {
				current = current + 1;
			} else if (ratings[i-1] == ratings[i]) {
				current = 1;
			} else {
				if (current == 1) {
					/***************/
				} else {
					current = 1;
				}
			}
			n += current;			
        }
        return n;
    }
};

int main( )
{
    cout<<"This is a C++ program.\n";
	Solution s;
	//int rArray[3] = {2,3,2}; 
	//int rArray[5] = {5,4,3,2,1};
	int rArray[6] = {1,3,4,3,2,1};
	vector<int> ratings(rArray, rArray + sizeof(rArray)/sizeof(int));
	cout<<"Correct solution:\n";
	cout << s.candy(ratings);
	cout<<"\nMy candy2:\n";
	cout << s.candy2(ratings);			
	cout<<"\nMy solution:\n";
	cout << s.myWrongSolution(ratings);			
    return 0;
}