  
## 003.Longest_Substring_Without_Repeating_Characters  
  
### **链接**：  
题目：https://leetcode.com/problems/Longest-Substring-Without-Repeating-Characters/  
代码(github)：https://github.com/JianghanLi/LeetCode  
  
### **题意**：  
求一个字符串中最长的不含重复字符的子串。
  
### **分析**：
题目中有两个要点：1.不含重复字符 2.最长。
- 不含重复：用长度为128(ACSII)或256(拓展ACSII)的数组或散列表记录字符的出现情况。
- 最长：得新的子串，更新最大值。
	
0. 显然用暴力查找会有一个复杂度为O(n^2)的解法：遍历字符串的每个字符，以它为子串起点求子串长度再进行比较得最大值。
1. 降低复杂度的方法是遍历字符串的每个字符，以它为子串的终点，求子串长度，再进行比较。这样做的原因是在之前遍历的过程中，我们理应可以得到与这个子串相关的所有信息，判断子串起点的位置。
此子串起点可以根据前一个子串的起点位置做判断，所以为：max(前面最近出现此子串终点字符的位置的后一位, 前一个子串的起点)。
	- 开一个长度为128(ACSII)或256(拓展ACSII)的数组，记录当前字符最近出现的位置。
	- 遍历一遍字符串，根据当前字符出现情况更新子串起点，并同时更新长度最大值就行了。  
	时间复杂度O(n)，空间复杂度O(1)。
2. 动态规划：
	可以把1中的思路以动态规划的方式编程。dp[i]储存以第i个字符串作为结尾的子串的起点位置。dp[i] = max (dp[i-1], occurrence[s[i]] + 1);

---  
  
**(English version)**  
  
  
## 003.Longest_Substring_Without_Repeating_Characters  
  
  
**Link**:  
Problem: https://leetcode.com/problems/Longest-Substring-Without-Repeating-Characters/  
Newest solutions in my Github: https://github.com/JianghanLi/LeetCode  
  
**Analysis**：  
Generate an array of size 128(ACSII) or 256(extended ACSII) to record the last position of current character.  
Traverse the string and update the left bound according to occurrence of each char, and calculate the maximum.  
It will just cost constant space.