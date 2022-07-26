<pre><code>
<b>Algorithm</b> TwoSum(S, k):
    <i><b>Input:</b></i> A sorted Sequence S of length n and integer k
    <i><b>Output:</b></i> A tuple containing a pair of elements of S whose sum equals k.
            If no such pair exists, return a flag value like (None, None)
    <b>if</b> n <= 1 <b>then</b>
        <b>return</b> (None, None)
    <b>else if</b> S[0] + S[n-1] == k <b>then</b>
        <b>return</b> (S[0], S[n-1])
    <b>else if</b> S[0] + S[n-1] < k <b>then</b>
        <b>return</b> TwoSum(S[1:n], k)
    <b>else</b>
        <b>return</b> TwoSum(S[0:n-1], k) 
</code></pre>

This recursive algorithm has $O(n)$ time and space complexity. In the worse case, it makes between
$n - 1$ recursive calls to itself. Furthermore, it is $\Omega(1)$ in time and space complexity. In the best case, it
finds the pair during the initial call.
