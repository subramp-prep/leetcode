## 150. Evaluate Reverse Polish Notation (Medium)

### **链接**：
题目：https://leetcode.com/problems/evaluate-reverse-polish-notation/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
求一个逆波兰式的值。

### **分析**：
很经典的栈应用题。
思路是将数字推入栈中，遇到运算符再取出运算。
P.S.
	- 此题无需考虑运算符优先级，已经在波兰式中处理。
	- 对字符串的处理，Python: `int()`，C++/C: `atoi()`，Java: `Integer.parseInt()`。  
	- 需要注意的是 Python 的 `/` 操作。

### **相似问题**：
[227. Basic Calculator II](../227.Basic_Calculator_II)