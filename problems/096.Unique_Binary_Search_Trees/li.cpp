#include <cstdio>
#include <iostream>
using namespace std;

class Solution {
 public:
  int numTrees(int n) {
    int dp[n + 2];
    for (int i = 2; i <= n + 1; i++) dp[i] = 0;
    dp[0] = 1;
    for (int i = 2; i <= n + 1; i++) {
      for (int j = i - 1; j >= 0; j--) {
        dp[j] = dp[j + 1] + (j > 0 ? dp[j - 1] : 0);
      }
      // for (int i = 0; i <= n + 1; i++) cout << dp[i] << " ";
      // cout << endl;
    }

    return dp[0];
  }
};

int main() {
  Solution* s = new Solution();
  cout << s->numTrees(5) << endl;
  return 1;
}

// dp[i]记录右节点长度为i+1的树的个数
// n=1 1 0 0 0 0 0 0
// n=2 1 1 0 0 0 0 0
// n=3 2 2 1 0 0 0 0
// n=4 5 5 3 1 0 0 0
// n=5 14 14 9 4 1 0 0
// n=6 42 42 28 14 5 1 0