Function example3 can be found in exercises.py located in the vendor files for ch03.

Let us count array reads and addition as our primitive operations. The body of loop k runs
$1 + 2 + ... + n = \frac{n(n+1)}$ times (see Proposition 3.21 on page 139). Hence, there are $\frac{n(n+1)}{2}$
primitive operations in the worst case and example3 is $O(n^{2})$.
