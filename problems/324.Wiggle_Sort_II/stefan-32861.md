3 lines Python, with Explanation / Proof | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  15574 

<h2>Solution</h2>
<p>Roughly speaking I put the smaller half of the numbers on the even indexes and the larger half on the odd indexes.</p>
<pre><code>def wiggleSort(self, nums):
    nums.sort()
    half = len(nums[::2])
    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
</code></pre>
<p>Alternative, maybe nicer, maybe not:</p>
<pre><code>def wiggleSort(self, nums):
    nums.sort()
    half = len(nums[::2]) - 1
    nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
</code></pre>
<hr/>
<h2><strong>Explanation / Proof</strong></h2>
<p>I put the smaller half of the numbers on the even indexes and the larger half on the odd indexes, both from right to left:</p>
<pre><code>Example nums = [1,2,...,7]      Example nums = [1,2,...,8] 

Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
--------------------------      --------------------------
Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5
</code></pre>
<p>I want:</p>
<ul>
<li>Odd-index numbers are larger than their neighbors.</li>
</ul>
<p>Since I put the larger numbers on the odd indexes, clearly I already have:</p>
<ul>
<li>Odd-index numbers are larger than <strong>or equal to</strong> their neighbors.</li>
</ul>
<p>Could they be "equal to"? That would require some number M to appear both in the smaller and the larger half. It would be the largest in the smaller half and the smallest in the larger half. Examples again, where S means some number smaller than M and L means some number larger than M.</p>
<pre><code>Small half:  M . S . S . S      Small half:  M . S . S . S .
Large half:  . L . L . M .      Large half:  . L . L . L . M
--------------------------      --------------------------
Together:    M L S L S M S      Together:    M L S L S L S M
</code></pre>
<p>You can see the two M are quite far apart. Of course M could appear more than just twice, for example:</p>
<pre><code>Small half:  M . M . S . S      Small half:  M . S . S . S .
Large half:  . L . L . M .      Large half:  . L . M . M . M
--------------------------      --------------------------
Together:    M L M L S M S      Together:    M L S M S M S M
</code></pre>
<p>You can see that with seven numbers, three M are no problem. And with eight numbers, four M are no problem. Should be easy to see that in general, with n numbers, floor(n/2) times M is no problem. Now, if there were more M than that, then my method would fail. But... it would also be impossible:</p>
<ul>
<li>If n is even, then having more than n/2 times the same number clearly is unsolvable, because you'd have to put two of them next to each other, no matter how you arrange them.</li>
<li>If n is odd, then the only way to successfully arrange a number appearing more than floor(n/2) times is if it appears exactly floor(n/2)+1 times and you put them on all the even indexes. And to have the wiggle-property, all the other numbers would have to be larger. But then we wouldn't have an M in both the smaller and the larger half.</li>
</ul>
<p>So if the input has a valid answer at all, then my code will find one.</p> 

Ref: https://discuss.leetcode.com/topic/32861
