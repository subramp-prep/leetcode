A little explanation on GCD method. C++/Java/Python | LeetCode Discuss
============================
**Author:**  ShuangquanLi
**Reputation:**  142 

<p>only thing we should proof is this:</p>
<pre><code>if x and y are coprime,  then we can and only can reach every integer z in [0, x + y]. (1)
</code></pre>
<p>then for a GCD <code>g</code>, from <code>gx</code> and <code>gy</code>,<br/>
we can and only can reach every <code>z</code> in <code>{i * g | i in [0, x + y] }</code></p>
<p>now, let's see how to proof (1).<br/>
let x be the less one, and y the greater one.<br/>
then fill the two jug to full, we have <code>x</code> and <code>y</code> water each and <code>x + y</code> water in total.<br/>
then we pour out x water each time until we can't.</p>
<p>now we have these different z:</p>
<pre><code> y + x,  y,  y - x,  y - 2x, ... , y % x 
</code></pre>
<p>finally we have <code>y % x</code> water left, we pour it into the x jug,<br/>
then fill the y jug to full.<br/>
now the two jugs have <code>y % x</code> and  <code>y</code> water separately,<br/>
and <code>y + y % x</code> water in total.<br/>
then we pour from y jug into x jug until the x jug is full,<br/>
afterwards do the same thing like before,<br/>
to pour out x water each time until we can't.</p>
<p>finally we get <code>(y + y % x) % x = (y % x + y % x) % x = (2y) % x</code>  water left.</p>
<p>now we have these different z:</p>
<pre><code> y + y % x,   y + y % x - x,  y + y % x - 2x, ... ,  (2y) % x 
</code></pre>
<p>do this x times, we get z:</p>
<pre><code> y + (2y) % x,  y + (2y) % x - x, y + (2y) % x - 2x, ..., (3y) % x
 :
 :
 :    
 y + ((x-1)y) % x,  y + ((x-1)y) % x - x,  y + ((x-1)y) % x - 2x, ... ,  (xy) % x
</code></pre>
<p>then you see <code>(xy) % x = 0</code>, and</p>
<pre><code> y % x, (2y) % x, (3y) % x, ... , ((x-1)y) % x just are 1, 2, 3, 4, 5, ... , x - 1. (2)
</code></pre>
<p>proof for (2):<br/>
modulo x could get x - 1 different results at most exclusive 0, that's 1,2,3,...,x-1.<br/>
we have x - 1 expressions, suppose there is two same,<br/>
let a != b in [1, x-1] and <code>(ay) % x = (by) % x</code>,<br/>
then we get <code>((a - b)y) % x = 0</code>,<br/>
then <code>((a - b) % x) * (y % x) = 0</code>, <code>(a - b) % x = 0</code>.<br/>
for <code>1 &lt;= a, b &lt;= x - 1</code>, so we get <code>a = b</code>. it's impossible.</p>
<p>so we can get any z in [0, x + y]  water for coprime x and y.</p>
<p>C++ code:</p>
<pre><code>bool canMeasureWater(int x, int y, int z) {
    return z == 0 || z &lt;= (long long)x + y &amp;&amp; z % __gcd(x, y) == 0;
}
</code></pre>
<p>Java code:</p>
<pre><code>public boolean canMeasureWater(int x, int y, int z) {
    return z == 0 || (long)x + y &gt;= z &amp;&amp; z % gcd(x, y) == 0;
}
public int gcd(int x, int y) {
    return y == 0 ? x : gcd(y, x % y);
}
</code></pre>
<p>Python code:</p>
<pre><code>def canMeasureWater(self, x, y, z):
    from fractions import gcd
    return z == 0 or x + y &gt;= z and z % gcd(x, y) == 0
</code></pre>
<p>p.s. the testcases are too weak.<br/>
you may get overflow without long long, say 2147483647, 234524287, 1.<br/>
some code get AC, while runs wrong on this 4,6,8.</p> 

Ref: https://discuss.leetcode.com/topic/49262
