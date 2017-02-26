## 445.Add Two Numbers II (Medium)

### **链接**：
题目：https://leetcode.com/problems/add-two-numbers-ii/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给出两个表示整数的链表，求和。head是最高位，next是更低位

### **分析**：
此题的难点在于链表的单向性，所代表的整数只能从最高位开始读取，而加法存在进位的问题，要求从低位向高位读取。所以解题的关键在于如何反向读取链表中的值。
1. 将链表转化为可以反向取值的数据结构再进行计算：
	- 转化为整数相加再转化为链表：思路上可行，但是有的test case的值会导致long long溢出，造成结果错误
	- 存入array或string或stack再处理，改变取值方向，空间复杂度为O(n)
2. 创立反转的中间链表：
	先得两链表长度，正序对位取值相加，并建立新链表反向存储各位数未进位的和。再正序读取此链表处理进位，优势是空间复杂度降为O(1)
3. 递归法