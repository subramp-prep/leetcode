## 328.Odd Even Linked List (Medium)

### **链接**：
题目：https://leetcode.com/problems/odd-even-linked-list/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
把所有的偶节点都取出按次序接到list末尾。要求空间复杂度O(1)。

### **分析**：
思路就是将偶节点按顺序取出再放到list末尾。由于空间复杂度的限制，不能创建新的链表作为结果，要在现有链表上改造。
	- 将偶节点都取出自身相连，再连接到奇节点链条的尾端是最简单的思路。
	- 若每取出一个偶节点就连到直接末尾，遍历指针遇到加入的第一个偶节点停止，要注意处理末节点是奇是偶。