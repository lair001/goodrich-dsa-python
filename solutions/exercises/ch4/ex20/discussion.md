<pre><code>
<b>Algorithm</b> KSort(S, k):
    <i><b>Input:</b></i> An unsorted Sequence S of length n and integer k
    <i><b>Output:</b></i> The Sequence S sorted such that elements <= k come
            before elements > k
    <b>if</b> S[0] <= k <b>then</b>
        KSort(S[1:n], k)
        <b>return</b> S
    <b>else if</b> n <= 1 <b>then</b>
        <b>return</b> S
    <b>else if</b> S[n-1] <= k <b>then</b>
        <b>swap</b>(S[0], S[n-1])
        KSort(S[1:n-1], k)
        <b>return</b> S 
    <b>else</b>
        KSort(S[0:n-1])
        <b>return</b> S 
</code></pre>

This recursive algorithm has $\theta(n)$ time and space complexity. It makes between
$n//2$ and $n - 1$ recursive calls to itself.