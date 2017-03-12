## 483. Smallest Good Base (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/smallest-good-base/  
代码(github)：https://github.com/JianghanLi/LeetCode  
  
### **题意**：  
输入[3, 10^18]中的数，要求转化为所有位值均为1的k进制数。求此最小k。  
  
### **分析**：
1. 暴力搜索：时间复杂度O(nlogn)，空间复杂度O(1)。
	* 显然可以遍历小于n的数为进制基数，并判断此进制数是否所有位均为1，但是会超时。
	
2. 优化暴力搜索：时间复杂度：未知，空间复杂度O(1)
	* 做一步思维转换，可以将遍历的范围缩小到logn：k最小 <=> k进制数位数最多。
	* k进制数最大可能位数：log(n, 2)。递减遍历k进制可能位数：
		* 按照k进制数可能位数来得到相应的k，然后再判断是否所有位均为1
		* 在判断是否所有位均为1时，因为已经有了位数的信息，所以可以用等比数列公式判断
	* P.S.
		* 因为程序中用到了log，时间复杂度取决于所使用的语言和编译器，无法判断。
		* 最大输入值为10^18，log(10^18, 2)约为60。可以直接使用60作为最大可能位数。复杂度可降为O(1)。
		* [pow的复杂度默认为O(1)](http://stackoverflow.com/questions/13418180/time-complexity-of-c-math-library-pow-function)