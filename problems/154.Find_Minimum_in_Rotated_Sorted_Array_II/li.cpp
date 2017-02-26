class Solution {
public:
    int findMin(vector<int> &num) {
        int size = num.size();

        if(size == 0) {
            return 0;
        } else if(size == 1) {
            return num[0];
        } else if(size == 2) {
            return min(num[0], num[1]);
        }

        int start = 0;
        int stop = size - 1;
        
        //首先找到首尾数值不同的情况，再开始快速的二分法。避免数组有大量重复数字，而变成O(n)的算法。
        while(num[start] == num[stop]) {
            if(start == stop) { //考虑到整条数组都相等的情况
                return num[start];
            }
            int mid = start + (stop - start) / 2;
            if(num[mid] > num[start]) {
                start = mid;
            } else if(num[mid] < num[start]) {
                stop = mid;
            } else {
                start++;
            }
        }
        
		
		//和答案不同点在于，优化了num[mid] ＝= num[start]的情况。前提条件是初始条件是num[start] != num[end]
        while(start < stop - 1) {
            if(num[start] < num[stop]) {
                return num[start];
            }
            int mid = start + (stop - start) / 2;
            if(num[mid] >= num[start]) {
                start = mid;
            } else if (num[mid] < num[start]) {
                stop = mid;
            }
        }

        return min(num[start], num[stop]);
    }
};