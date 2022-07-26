<pre><code>
<b>Algorithm</b> FindMax(S):
    <i><b>Input:</b></i> Sequence S of length n
    <i><b>Output:</b></i> The maximum element in S
    <b>if</b> n == 0 <b>then</b>
        <b>return</b> None
    <b>else if</b> n == 1 <b>then</b>
        <b>return</b> S[n-1]
    <b>else</b>
        <b>return</b> Maximum of S[n-1] and FindMax(S[0:n-1])
</code></pre>

This recursive algorithm has $\theta(n)$ time and space complexity. Each element is considered once and the algorithm
makes $n-1$ recursive calls to itself. However, the underlying problem has $\theta(n)$ time and $\theta(1)$ space
complexity since it can be solved using an iterative algorithm with constant memory usage.
