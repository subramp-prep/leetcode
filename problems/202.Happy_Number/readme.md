## 202. Happy Number (Easy)

### **链接**：
题目：https://leetcode.com/submissions/detail/26084443/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

给一个操作，每次对一个数的每一位平方求和。  
现在给一个数，对这个数循环操作，如果这个数可以变成 1，那这个数就是 Happy Number。  
问这个数是不是 Happy Number。

### **分析**：

1. 可以用 HashMap 记录已经出现过的数，若此数再次出现，说明计算存在循环，则一定不为Happy Number
2. 快慢指针：参考 [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) 的 [Two Point 解法](https://github.com/JianghanLi/LeetCode/tree/master/solutions/141.Linked_List_Cycle) 来做。
	- 比起解法1可以省去hash map的空间。本质上还是判断是否计算存在循环，即某数是否重复出现。
3. 数学可得[Happy Number数列的收敛方式](https://en.wikipedia.org/wiki/Happy_number#Sequence_behavior)，由其特点可得两个解法：
	1. 非快乐数一定进入4, 16, 37, 58, 89, 145, 42, 20, 4, ...的循环：
		- 得到1时，返回true。得到4时返回false。
		- 又因为2, 3, 4, 5, 6均不为Happy Number，故可以稍稍扩大返回false的判断范围（<=6）。
	2. 大于1000的数会指数级收敛到1000以下，并在<=3次计算之后，收敛到100以内：
		- 穷举100以内的Happy Number。
		- 待收敛到100以下再比较

根据其收敛方式可得, 时间复杂度为O(logn)。  

Quote from Wikipedia:  
Note that if n has m digits, then the sum of the squares of its digits is at most 9^2 m, or 81m.  
For m=4 and above,  
n >= 10^(m-1) > 81m  
so any number over 1000 gets smaller under this process and in particular becomes a number with strictly fewer digits. Once we are under 1000, the number for which the sum of squares of digits is largest is 999, and the result is 3 times 81, that is, 243.  
In the range 100 to 243, the number 199 produces the largest next value, of 163.  
In the range 100 to 163, the number 159 produces the largest next value, of 107.  
In the range 100 to 107, the number 107 produces the largest next value, of 50.  
Considering more precisely the intervals [244,999], [164,243], [108,163] and [100,107], we see that every number above 99 gets strictly smaller under this process. Thus, no matter what number we start with, we eventually drop below 100. An exhaustive search then shows that every number in the interval [1,99] either is happy or goes to the above cycle (4, 16, 37, 58, 89, 145, 42, 20, 4....).  
The above work produces the interesting result that no positive integer other than 1 is the sum of the squares of its own digits, since any such number would be a fixed point of the described process.  
From the above proving process from Wikipedia, we know that for any number, no matter what number we start, we eventually drop below 100. So we don't need to store all previous number, we just need to store the number that's less than 100. A number which is larger than 100 cannot become a part of the circle. So that we at most store 100 numbers in the HashSet, that makes the space complexity constant.  
Time Complexity: O(log*n) or almost O(1)   Space Complexity: O(1)  