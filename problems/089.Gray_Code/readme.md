## 089. Gray Code (Medium) 
  
### **链接**：  
题目：https://leetcode.com/problems/gray-code/  
代码(github)：https://github.com/JianghanLi/LeetCode  

<h1>题目：</h1> 
<p></p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> The gray code is a binary numeral system where two successive values differ in only one bit.</p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> Given a non-negative integer&nbsp;<span style="">n</span>&nbsp;representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.</p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> 格雷码是一个二进制数字系统，两个连续的数字的二进制数字只有一位不同。<br> </p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> 给定一个非负整数n，代表格雷码的二进位的个数，输出格雷码序列。格雷码序列必须以0开头。</p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> For example, given&nbsp;<span style="">n</span>&nbsp;= 2, return&nbsp;<code style="font-family:Menlo,Monaco,Consolas,&#39;Courier New&#39;,monospace; font-size:13px; padding:2px 4px; color:rgb(199,37,78); background-color:rgb(249,242,244)">[0,1,3,2]</code>. Its gray code sequence is:</p> 
<pre style="overflow:auto; font-family:Menlo,Monaco,Consolas,&#39;Courier New&#39;,monospace; font-size:13px; padding:9.5px; margin-top:0px; margin-bottom:10px; line-height:1.42857143; color:rgb(51,51,51); word-break:break-all; word-wrap:break-word; background-color:rgb(245,245,245); border:1px solid rgb(204,204,204)" class="hljs">00 - 0
01 - 1
11 - 3
10 - 2
</pre> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> <span style="font-weight:700">Note:</span><br style=""> For a given&nbsp;<span style="">n</span>, a gray code sequence is not uniquely defined.</p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> For example,&nbsp;<code style="font-family:Menlo,Monaco,Consolas,&#39;Courier New&#39;,monospace; font-size:13px; padding:2px 4px; color:rgb(199,37,78); background-color:rgb(249,242,244)">[0,2,3,1]</code>&nbsp;is also a valid gray code sequence according to the above definition.</p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.</p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> 对于给定的数字n，格雷码不是唯一的。</p> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> 格雷码：<a target="_blank" href="http://baike.baidu.com/link?url=YnRSupt_rTOzFEM5PENs1hbds0VBu-0ay3KWZc5C5NTx4wR13-ALLLzWglja-nZ-rRlkw_FQSU9IBc0MdS0uuq" rel="nofollow">http://baike.baidu.com/link?url=YnRSupt_rTOzFEM5PENs1hbds0VBu-0ay3KWZc5C5NTx4wR13-ALLLzWglja-nZ-rRlkw_FQSU9IBc0MdS0uuq</a>&nbsp;。</p> 
<h1>思路：</h1> 
<p style="margin-top:0px; margin-bottom:10px; color:rgb(51,51,51); font-family:&#39;Helvetica Neue&#39;,Helvetica,Arial,sans-serif; font-size:14px; line-height:30px"> </p> 
<p>自然二进制码转换为格雷码：g 0 = b 0 , g i = b i ⊕ b i − 1<br> 保留自然二进制码的最高位作为格雷码的最高位（首位），格雷码次高位为二进制码的高位与次高位异或，其余各位与次高位的求法类似。例如，将自然二进制码1001，转换为格雷码的过程是：保留最高位；然后将第1 位的1 和第2 位的0 异或，得到1，作为格雷码的第2 位；将第2 位的0 和第3 位的0 异或，得到0，作为格雷码的第3 位；将第3 位的0 和第4 位的1 异或，得到1，作为格雷码的第4 位，最终，格雷码为1101。<br> 格雷码转换为自然二进制码：b 0 = g 0 , b i = g i ⊕ b i − 1<br> 保留格雷码的最高位作为自然二进制码的最高位，次高位为自然二进制高位与格雷码次高位异或，其余各位与次高位的求法类似。例如，将格雷码1000 转换为自然二进制码的过程是：保留最高位1，作为自然二进制码的最高位；然后将自然二进制码的第1 位1 和格雷码的第2 位0 异或，得到1，作为自然二进制码的第2 位；将自然二进制码的第2 位1 和格雷码的第3 位0 异或，得到1，作为自然二进制码的第3 位；将自然二进制码的第3 位1 和格雷码的第4 位0 异或，得到1，作为自然二进制码的第4 位，最终，自然二进制码为1111。

<br><span style="color:red">格雷码有数学公式，整数</span><span style="color:red"> n </span><span style="color:red">的格雷码是</span><span style="color:red"> n </span><span style="color:red">⊕</span><span style="color:red"> ( n/2)</span><span style="color:red">。(实际是由n的自然二进制码转换为格雷码，然后由格雷码转换为十进制数，比如上面的1001-&gt;1101)</span><br>

这题要求生成 n 比特的所有格雷码。<br> 方法 1，最简单的方法，利用数学公式，对从0 ∼ 2 ^n − 1 的所有整数，转化为格雷码。<br> 方法 2，n 比特的格雷码，可以递归地从n − 1 比特的格雷码生成。</p> 
<p></p> 
<p>这种方法基于格雷码是反射码的事实，利用递归的如下规则来构造：</p> 
<p>1位格雷码有两个码字</p> 
<p>(n+1)位格雷码中的前2^n个码字等于n位格雷码的码字，按顺序书写，加前缀0</p> 
<p>(n+1)位格雷码中的后2^n个码字等于n位格雷码的码字，按逆序书写，加前缀1</p> 
<br> 
<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Binary-reflected_Gray_code_construction.svg/250px-Binary-reflected_Gray_code_construction.svg.png" alt=""><br> </p> 
<h1>&nbsp;代码1（公式法）：</h1> 
<p></p> 
<pre name="code" class="cpp hljs"><span class="hljs-keyword">class</span> Solution {
<span class="hljs-keyword">public</span>:
    <span class="hljs-comment">//整数 n 的格雷码是 n ⊕ ( n/2) </span>
    <span class="hljs-stl_container"><span class="hljs-built_in">vector</span>&lt;<span class="hljs-keyword">int</span>&gt;</span> grayCode(<span class="hljs-keyword">int</span> n) 
    {
        <span class="hljs-keyword">int</span> num = <span class="hljs-number">1</span> &lt;&lt; n;
        <span class="hljs-stl_container"><span class="hljs-built_in">vector</span>&lt;<span class="hljs-keyword">int</span>&gt;</span> result;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span> ; i &lt; num ; i++)
        {
            result.push_back(i ^ (i &gt;&gt; <span class="hljs-number">1</span>));
        }
        <span class="hljs-keyword">return</span> result;
    }
};</pre> 
<br> 
<p></p> 
<h1>代码2：</h1> 
<p></p> 
<p> </p> 
<table class="table-view log-set-param " style="border-collapse:collapse; border-spacing:0px; margin:5px 0px; word-wrap:break-word; word-break:break-all; font-size:12px; line-height:22px; color:rgb(0,0,0); font-family:arial,宋体,sans-serif"> 
 <tbody> 
  <tr> 
   <th style="margin:0px; padding:2px 10px; height:23px; border:1px solid rgb(230,230,230); text-align:center; background-color:rgb(249,249,249)"> 2位格雷码</th> 
   <th style="margin:0px; padding:2px 10px; height:23px; border:1px solid rgb(230,230,230); text-align:center; background-color:rgb(249,249,249)"> 3位格雷码</th> 
   <th style="margin:0px; padding:2px 10px; height:23px; border:1px solid rgb(230,230,230); text-align:center; background-color:rgb(249,249,249)"> 4位格雷码</th> 
   <th style="margin:0px; padding:2px 10px; height:23px; border:1px solid rgb(230,230,230); text-align:center; background-color:rgb(249,249,249)"> 4位自然二进制码</th> 
  </tr> 
  <tr> 
   <td align="left" valign="center" style="margin:0px; padding:2px 10px; height:22px; border:1px solid rgb(230,230,230)"> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      00 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      01 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      11 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      10 
    </div> </td> 
   <td align="left" valign="center" style="margin:0px; padding:2px 10px; height:22px; border:1px solid rgb(230,230,230)"> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      000 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      001 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      011 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      010 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      110 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      111 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      101 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      100 
    </div> </td> 
   <td align="left" valign="center" style="margin:0px; padding:2px 10px; height:22px; border:1px solid rgb(230,230,230)"> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0000 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0001 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0011 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0010 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0110 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0111 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0101 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0100 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1100 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1101 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1111 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1110 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1010 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1011 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1001 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1000 
    </div> </td> 
   <td align="left" valign="center" style="margin:0px; padding:2px 10px; height:22px; border:1px solid rgb(230,230,230)"> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0000 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0001 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0010 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0011 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0100 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0101 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0110 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      0111 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1000 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1001 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1010 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1011 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1100 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1101 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1110 
    </div> 
    <div class="para" style="color:rgb(51,51,51); margin:0px; line-height:24px">
      1111 
    </div> 
    <div> 
     <br> 
    </div> </td> 
  </tr> 
 </tbody> 
</table> 
<br> 
<p></p> 
<p></p>

<pre name="code" class="cpp hljs"><span class="hljs-keyword">class</span> Solution {
<span class="hljs-keyword">public</span>:
    <span class="hljs-stl_container"><span class="hljs-built_in">vector</span>&lt;<span class="hljs-keyword">int</span>&gt;</span> grayCode(<span class="hljs-keyword">int</span> n) 
    {
        <span class="hljs-stl_container"><span class="hljs-built_in">vector</span>&lt;<span class="hljs-keyword">int</span>&gt;</span> result;
        result.push_back(<span class="hljs-number">0</span>);
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i &lt; n; i++) 
        {
            <span class="hljs-keyword">const</span> <span class="hljs-keyword">int</span> highest_bit = <span class="hljs-number">1</span> &lt;&lt; i;<span class="hljs-comment">//2^i位的前2^(i-1)位不需要改变，后2^(i-1)位为用1&lt;&lt;i与前2^(i-1)位的逆序取或</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> j = result.size() - <span class="hljs-number">1</span>; j &gt;= <span class="hljs-number">0</span>; j--) <span class="hljs-comment">// 要反着遍历，才能对称</span>
            {
                result.push_back(highest_bit | result[j]);
            }
        }
        <span class="hljs-keyword">return</span> result;
    }
};</pre>
                
<a href="http://blog.csdn.net/u012243115/article/details/42486895" target="_blank" rel="nofollow">原文链接</a>