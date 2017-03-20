4 lines C, 6 lines Ruby, 7 lines Python, 1-liners
========

<div class="content" component="post/content" itemprop="text">
    <p>Same O(m+n) method as most, just a bit different style/languages.</p>
    <hr>
    <p><strong>C</strong></p>
    <p>Check the top-right corner. If it's not the target, then remove the top row or rightmost column.</p>
    <pre class="markdown-highlight"><code class="hljs cpp"><span class="hljs-function"><span class="hljs-keyword">bool</span> <span class="hljs-title">searchMatrix</span><span class="hljs-params">(<span class="hljs-keyword">int</span>** A, <span class="hljs-keyword">int</span> m, <span class="hljs-keyword">int</span> n, <span class="hljs-keyword">int</span> target)</span> </span>{
    <span class="hljs-keyword">int</span> x = ~target;
    <span class="hljs-keyword">while</span> (m &amp;&amp; n &amp;&amp; (x = A[<span class="hljs-number">0</span>][n<span class="hljs-number">-1</span>]) != target)
        x &lt; target ? A++, m-- : n--;
    <span class="hljs-keyword">return</span> x == target;
}
</code></pre>
    <p><strong>Ruby</strong></p>
    <pre class="markdown-highlight"><code class="hljs ruby"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">search_matrix</span><span class="hljs-params">(matrix, target)</span></span>
    j = -<span class="hljs-number">1</span>
    matrix.each { <span class="hljs-params">|row|</span>
        j -= <span class="hljs-number">1</span> <span class="hljs-keyword">while</span> row[j] &amp;&amp; row[j] &gt; target
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span> <span class="hljs-keyword">if</span> row[j] == target
    }
    <span class="hljs-literal">false</span>
<span class="hljs-keyword">end</span>
</code></pre>
    <p><strong>Python</strong></p>
    <pre class="markdown-highlight"><code class="hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">searchMatrix</span><span class="hljs-params">(self, matrix, target)</span>:</span>
    j = <span class="hljs-number">-1</span>
    <span class="hljs-keyword">for</span> row <span class="hljs-keyword">in</span> matrix:
        <span class="hljs-keyword">while</span> j + len(row) <span class="hljs-keyword">and</span> row[j] &gt; target:
            j -= <span class="hljs-number">1</span>
        <span class="hljs-keyword">if</span> row[j] == target:
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">True</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">False</span>
</code></pre>
    <p><strong>1-liners</strong></p>
    <p>Relax, I know they're O(mn). This is just for fun (although they did get accepted):</p>
    <p>Python (204 ms):</p>
    <pre class="markdown-highlight"><code class="hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">searchMatrix</span><span class="hljs-params">(self, matrix, target)</span>:</span>
    <span class="hljs-keyword">return</span> any(target <span class="hljs-keyword">in</span> row <span class="hljs-keyword">for</span> row <span class="hljs-keyword">in</span> matrix)
</code></pre>
    <p>Ruby (828 ms):</p>
    <pre class="markdown-highlight"><code class="hljs ruby"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">search_matrix</span><span class="hljs-params">(matrix, target)</span></span>
    matrix.any? { <span class="hljs-params">|row|</span> row.<span class="hljs-keyword">include</span>? target }
<span class="hljs-keyword">end</span></code></pre>

</div>