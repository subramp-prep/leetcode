#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findPeakElement(const vector<int> &num) {
        for(int i = 0; i < num.size()-1; i ++) if(num[i+1] < num[i]) return i;
        return num.size()-1;
    }
};

int main() {
  Solution s;
  cout << s.findPeakElement({1,2,3,1}) << endl;
}