## 227. Basic Calculator II (Medium)

### **链接**：
题目：https://leetcode.com/problems/basic-calculator-ii
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
计算带有+-*/和正整数的字符串。

### **分析**：
难点是乘除法的优先级要高于加减法。注意字符串中的空格。
	1. 可以用stack储存所有要相加的数，遇到加减放入stack，乘除更换最上层的数
	2. 也可以不用stack，因为只用保留最后一项来进行乘除法
	3. 利用istringstream可以自动处理空格和数字的特点，简化取数的过程。