
## 004.Median_of_Two_Sorted_Arrays

### **链接**：
题目：https://leetcode.com/problems/Median-of-Two-Sorted-Arrays/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
求两个有序数组的中位数。要求复杂度是 O(log(n + m))。

### **分析**：
若不要求结果复杂度，则有很简单的答案：
0. 直接 merge 两个数组，然后求中位数，复杂度是 O(n + m)。 

题目的难点是降低答案复杂度。从中位数本身着手思考，有两种思路：
1. 从中位数的计算公式出发：若总个数为奇，是第 (1+n)/2 大的数， 若总个数为偶，是第 n/2 大和第 (n/2)+1 大的数的平均值
	分奇偶情况，转化思维，求两个有序数组中的第 K 大数 (二分法)，再计算中位数。
	题目转化为求两个数组中的第 K 大数，可用递归法求出：
		- 因为是第 K 大数，所以两个数组中，一定有一个数组前 K/2 个数不包括第K大数。=> 去掉这K/2个数，再求第 K-K/2 大数。
2. 从中位数的定义出发：大于中位数的数和小于中位数的数一样多
	将两个数组称为A, B, 再分别分为两个组A1, A2, B1, B2, len(A1)+len(B1)==len(A2)+len(B2) && A1, B1 < A2, B2。
	所以题目转化为求出A组和B组中的分界点，可用二分法求出：
		- B组界点位置可用A组界点位置表示
		- 终止条件：小组最大数 < 大组最小数
	若总个数为奇，中位数就是小组最大数，若为偶，则为小组最大数和大组最小数的平均值。

---

**(English version)*

## 004.Median_of_Two_Sorted_Arrays


**Link**:
Problem: https://leetcode.com/problems/Median-of-Two-Sorted-Arrays/  
Newest solutions in my Github: https://github.com/JianghanLi/LeetCode

**Analysis**：
Two ways to get it.  
1. Merge the two arrays first and solve it. But the time complexity is O(n + m).  
2. From formula of median, calculate it on 2 cases : odd or even number of elements.
The problem can then be seen as to find the k-th biggest number in two sorted arrays (by binary search).  
3. From the definition of median in statistics, we can divide the 2 arrays to form 2 subsets of equal length that one subset is always greater than the other
So if there are odd number of elements, the median will be max of smaller set, else, it will be (max of smaller set + min of greater set )/ 2