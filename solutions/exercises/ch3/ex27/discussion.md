Function example5 can be found in exercises.py located in the vendor files for ch03.

Let us count array reads and addition as our primitive operations. The body of loop k runs
$n(1 + 2 + ... + n) = n\frac{n(n+1)}{2} = \frac{n^{2}(n+1)}{2}$ times (see Proposition 3.21 on page 139). Also, the
body of loop i, which runs $n$ times, has an addition that occurs if $B[i] == total$. This runs $n$ times in the worst
case. Hence, there are $n^{2}(n+1) + n$ primitive operations in the worst case and example5 is $O(n^{3})$.
