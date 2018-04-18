#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, int> counter, first;
        int res = 0, degree = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (first.count(nums[i]) == 0) first[nums[i]] = i;
            if (++counter[nums[i]] > degree) {
                degree = counter[nums[i]];
                res = i - first[nums[i]] + 1;
            } else if (counter[nums[i]] == degree)
                res = min(res, i - first[nums[i]] + 1);
        }
        return res;
    }
};

int main() {
    Solution s;
    int nums[] = {1, 2, 2, 3, 1, 4, 2}; // 6
    vector<int> A(nums, nums + sizeof(nums) / sizeof(nums[0]));
    cout << s.findShortestSubArray(A) << endl;

    int nums2[] = {1, 2, 2, 3, 1} ; // 2
    vector<int> A2(nums2, nums2 + sizeof(nums2) / sizeof(nums2[0]));
    cout << s.findShortestSubArray(A2) << endl;
}


// 循环内要加 int i = 0, 不然i的初始值不可预料。