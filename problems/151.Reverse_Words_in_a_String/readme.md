## 151. Reverse Words in a String (Medium)

### **链接**：
题目：https://leetcode.com/problems/reverse-words-in-a-string/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
把一句话里的单词反向连接输出。要注意空格的处理。

### **分析**：
1. 若不要求空间复杂度为O(1)，则要考虑两个点：1. 如何处理空格，并得到单词字符串。2. 反转顺序
	i. **(C++)** 
		- 处理字符串空格的题目，都可以用 stringstream 简化得到每个单词字符串。
		- 然后反向连接（直接反向链接或者用stack）。
	空间复杂度为O(n)，时间复杂度 O(n)。

	ii. **(Java)** 用 `String` 的 `trim` 和 `split` 处理空格分成字符串数组，再反向连接。
	iii. **(Python)** 一句话就行了。

2. 在C语言中，要求空间复杂度为O(1)，这是个难点。
	**(C)** ，思路：
		- 反转每个单词字符串，并同时处理空格
		- 反转整个句子字符串
	空间复杂度为O(1)，时间复杂度同样是 O(n)。