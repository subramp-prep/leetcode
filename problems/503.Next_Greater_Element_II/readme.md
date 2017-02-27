## 503. Next Greater Element II (Medium)

### **链接**：
题目：https://leetcode.com/problems/next-greater-element-ii/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个可以看成环状的数组(尾首相连)，求每个值的下一个更大值组成的数组，没有更大值则为-1。

### **分析**：
1. 暴力搜索
	- 可以用求余来处理成环的搜索，很简洁
时间复杂度O(n2),空间复杂度O(1)

2. Stack：思路转换，遍历数组并按顺序向后寻找更大值(Brute force) -> 遍历数组并向前在stack中寻找将自己视为更大值的可填入的index(Stack)
	- 需要遍历两次：
		i.  栈不为空时，用while循环，比较当前值和栈顶index表示值的大小，若当前值大于栈顶index表示值，则将当前值填入index，并pop()。
			直到栈顶index表示值小于当前值，结束while循环，并将当前值的index推入栈中。
		ii. 同样的思路，但不再向栈中推值
	- 两次遍历之后还留在stack中的index，是那些没有更大值的数。
	P.S. 可以将两次遍历放入同一个 for 循环中，用mod处理让代码更简洁
时间复杂度O(n)，空间复杂度O(n)