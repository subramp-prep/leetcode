<div class="post-panel"><div class="post-info-bar"><div class="post-info" title="March 25, 2018 2:00 PM"><p>Last Edit: Mar 25, 2018, 2:00 PM</p></div><div class="user-info"><div class="avatar simple-avatar__1nLM hover-effect__2WOZ"><a href="/stefanpochmann" target="_blank"><img class="simp-avatar__mRN_" src="https://www.gravatar.com/avatar/0815eb7d4e9dd58022d51ba2011b9c0a.png?s=200" alt="StefanPochmann" data-has-link="true" style="height: 20px; width: 20px;"></a></div><div class="username" title="StefanPochmann"><a href="/stefanpochmann" target="_blank">StefanPochmann</a></div><span class="reputation-tip" data-toggle="tooltip" data-placement="top" data-original-title="Reputation" aria-hidden="true" style="cursor: pointer;"><div class="reputation"><i class="fa fa-star ation-icon" aria-hidden="true"></i>&nbsp;21020</div></span></div></div><p><p>There are so many different approaches and so many different ways to implement each. I find it hard to decide, so here are several :-)</p>
<p>In all of them, I check one of these tree characterizations:</p>
<ul>
<li>Has n-1 edges and is acyclic.</li>
<li>Has n-1 edges and is connected.</li>
</ul>
<hr>
<p><strong>Solution 1</strong> ... <strong>Union-Find</strong></p>
<p>The test cases are small and harmless, <a href="https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Disjoint-set_forests">simple union-find</a> suffices (runs in about 50~60 ms).</p>
<pre><code><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">validTree</span></span>(<span class="hljs-keyword">self</span>, n, edges):
    parent = range(n)
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">find</span></span>(x):
        <span class="hljs-keyword">return</span> x <span class="hljs-keyword">if</span> parent[x] == x <span class="hljs-keyword">else</span> find(parent[x])
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">union</span></span>(xy):
        x, y = map(find, xy)
        parent[x] = y
        <span class="hljs-keyword">return</span> x != y
    <span class="hljs-keyword">return</span> len(edges) == n-<span class="hljs-number">1</span> and all(map(<span class="hljs-class"><span class="hljs-keyword">union</span>, <span class="hljs-title">edges</span>))</span>
</code></pre>
<p>A version without using <code>all(...)</code>, to be closer to other programming languages:</p>
<pre><code><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">validTree</span><span class="hljs-params">(<span class="hljs-keyword">self</span>, n, edges)</span></span>:
    parent = range(n)
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">find</span><span class="hljs-params">(x)</span></span>:
        <span class="hljs-keyword">return</span> x <span class="hljs-keyword">if</span> parent[x] == x <span class="hljs-keyword">else</span> find(parent[x])
    <span class="hljs-keyword">for</span> e <span class="hljs-keyword">in</span> <span class="hljs-symbol">edges:</span>
        x, y = map(find, e)
        <span class="hljs-keyword">if</span> x == <span class="hljs-symbol">y:</span>
            <span class="hljs-keyword">return</span> False
        parent[x] = y
    <span class="hljs-keyword">return</span> len(edges) == n - <span class="hljs-number">1</span>
</code></pre>
<p>A version checking <code>len(edges) != n - 1</code> first, as <code>parent = range(n)</code> could fail for huge <code>n</code>:</p>
<pre><code><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">validTree</span></span>(<span class="hljs-keyword">self</span>, n, edges):
    <span class="hljs-keyword">if</span> len(edges) != n - <span class="hljs-number">1</span>:
        <span class="hljs-keyword">return</span> False
    parent = range(n)
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">find</span></span>(x):
        <span class="hljs-keyword">return</span> x <span class="hljs-keyword">if</span> parent[x] == x <span class="hljs-keyword">else</span> find(parent[x])
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">union</span></span>(xy):
        x, y = map(find, xy)
        parent[x] = y
        <span class="hljs-keyword">return</span> x != y
    <span class="hljs-keyword">return</span> all(map(<span class="hljs-class"><span class="hljs-keyword">union</span>, <span class="hljs-title">edges</span>))</span>
</code></pre>
<hr>
<p><strong>Solution 2</strong> ... <strong>DFS</strong></p>
<pre><code>def validTree(self, n, <span class="hljs-built_in">edges</span>):
    <span class="hljs-built_in">neighbors</span> = {i: [] <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(n)}
    <span class="hljs-keyword">for</span> v, w <span class="hljs-keyword">in</span> <span class="hljs-built_in">edges</span>:
        <span class="hljs-built_in">neighbors</span>[v] += w,
        <span class="hljs-built_in">neighbors</span>[w] += v,
    def visit(v):
        <span class="hljs-built_in">map</span>(visit, <span class="hljs-built_in">neighbors</span>.<span class="hljs-built_in">pop</span>(v, []))
    visit(<span class="hljs-number">0</span>)
    <span class="hljs-built_in">return</span> len(<span class="hljs-built_in">edges</span>) == n-<span class="hljs-number">1</span> <span class="hljs-keyword">and</span> <span class="hljs-keyword">not</span> <span class="hljs-built_in">neighbors</span>
</code></pre>
<p>Or check the number of edges first, to be faster and to survive unreasonably huge <code>n</code>:</p>
<pre><code>def validTree(self, n, <span class="hljs-built_in">edges</span>):
    <span class="hljs-keyword">if</span> len(<span class="hljs-built_in">edges</span>) != n - <span class="hljs-number">1</span>:
        <span class="hljs-built_in">return</span> False
    <span class="hljs-built_in">neighbors</span> = {i: [] <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(n)}
    <span class="hljs-keyword">for</span> v, w <span class="hljs-keyword">in</span> <span class="hljs-built_in">edges</span>:
        <span class="hljs-built_in">neighbors</span>[v] += w,
        <span class="hljs-built_in">neighbors</span>[w] += v,
    def visit(v):
        <span class="hljs-built_in">map</span>(visit, <span class="hljs-built_in">neighbors</span>.<span class="hljs-built_in">pop</span>(v, []))
    visit(<span class="hljs-number">0</span>)
    <span class="hljs-built_in">return</span> <span class="hljs-keyword">not</span> <span class="hljs-built_in">neighbors</span>
</code></pre>
<p>For an iterative version, just replace the three "visit" lines with</p>
<pre><code>    <span class="hljs-built_in">stack</span> = [<span class="hljs-number">0</span>]
    <span class="hljs-keyword">while</span> <span class="hljs-built_in">stack</span>:
        <span class="hljs-built_in">stack</span> += neighbors.pop(<span class="hljs-built_in">stack</span>.pop(), [])
</code></pre>
<hr>
<p><strong>Solution 3</strong> ... <strong>BFS</strong></p>
<p>Just like DFS above, but replace the three "visit" lines with</p>
<pre><code>    <span class="hljs-built_in">queue</span> = [<span class="hljs-number">0</span>]
    <span class="hljs-keyword">for</span> v in <span class="hljs-built_in">queue</span>:
        <span class="hljs-built_in">queue</span> += neighbors.pop(v, [])
</code></pre>
<p>or, since that is not guaranteed to work, the safer</p>
<pre><code>    <span class="hljs-built_in">queue</span> = collections.<span class="hljs-built_in">deque</span>([<span class="hljs-number">0</span>])
    <span class="hljs-keyword">while</span> <span class="hljs-built_in">queue</span>:
        <span class="hljs-built_in">queue</span>.extend(neighbors.pop(<span class="hljs-built_in">queue</span>.popleft(), []))</code></pre>
</p></div>