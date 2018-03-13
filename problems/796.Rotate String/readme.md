## 796.Rotate String (Easy)

### **链接**：
题目：https://https://leetcode.com/problems/rotate-string/  
代码(github)：https://github.com/JianghanLi/LeetCode  

### **题意**：
两个字符串A和B，问其中一个是不是另一个左右两部分substring互换得来的  

### **分析**：
主要是两种解法：  
1. 暴力搜索 O(n^2)
	- 寻找B[0]在A中的位置，并比较A此位置的左右两边互换是否为B
	- 模拟shift，一个一个字母从头连接在尾部再比较是否相同
2. 连接string并搜索另一个 O(n^2)
	- 利用rotate string的特点，若A和B互为rorate string，则两个A相连，其中必定包含B
	- 复杂度为string::find的复杂度，时间O(N*M)，空间O(1)
 
也可以使用KMP算法来比较string，降低复杂度