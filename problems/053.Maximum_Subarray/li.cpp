class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        return divide(nums, 0, nums.size() - 1, INT_MIN);
    }

    int divide(vector<int>& A, int left, int right, int tmax) {
        //本来效率比较低，所以加了left＝＝right条件，避免执行后半部分代码
		if(left == right) { 
            return A[left];
        }
        if(left > right) {
            return INT_MIN; //答案给的终点，但是不太好考虑，INT_MIN是c++保留字
        }

        int mid = left + (right - left) / 2;
        //得到子区间[left, mid - 1]最大值
        int lmax = divide(A, left, mid - 1, tmax);
        //得到子区间[mid + 1, right]最大值
        int rmax = divide(A, mid + 1, right, tmax);

        tmax = max(tmax, lmax);
        tmax = max(tmax, rmax);

        int sum = 0;
        int mlmax = 0;
        //得到[left, mid - 1]最大值
        for(int i = mid - 1; i >= left; i--) {
            sum += A[i];
            mlmax = max(mlmax, sum);
        }

        sum = 0;
        int mrmax = 0;
        //得到[mid + 1, right]最大值
        for(int i = mid + 1; i <= right; i++) {
            sum += A[i];
            mrmax = max(mrmax, sum);
        }

        tmax = max(tmax, A[mid] + mlmax + mrmax);
        return tmax;
    }
};