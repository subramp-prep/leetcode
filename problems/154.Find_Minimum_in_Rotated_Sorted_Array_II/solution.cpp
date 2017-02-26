/*
Find Minimum in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
这题跟上题唯一的区别在于元素可能有重复，我们仍然采用上面的方法，只是需要处理mid与start相等这种额外情况。

A[mid] > A[start]，右半区间查找。
A[mid] < A[start]，左半区间查找。
A[mid] = A[start]，出现这种情况，我们跳过start，重新查找，譬如[2,2,2,1]，A[mid] = A[start]都为2，这时候我们跳过start，使用[2,2,1]继续查找。
代码如下:
*/
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

        while(start < stop - 1) {
            if(num[start] < num[stop]) {
                return num[start];
            }

            int mid = start + (stop - start) / 2;
            if(num[mid] > num[start]) {
                start = mid;
            } else if(num[mid] < num[start]) {
                stop = mid;
            } else { //例如［10, 1, 10, 10, 10]的情况
                start++; //这题需要注意，如果重复元素很多，那么最终会退化到遍历整个数组，而不是二分查找了。
            }
        }

        return min(num[start], num[stop]);
    }
};