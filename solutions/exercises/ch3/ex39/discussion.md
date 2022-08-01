Running the script written using **Horner's method** (see ex 3.50) shows that this sum rapidly
converges to 2 from below. It hits the limits of double float precision somewhere between $n=32$
and $n=64$.

Unfortunately, although **Horner's method** allows us to efficiently demonstrate the relationship empirically in $O(n)$
time, it offers little insight into how to rigorously prove the relationship (at least I wasn't inspired by it).
However, based on a $O(n^2)$ algorithm, we may be inspired to try the following:

$\sum^n_{i=1} \frac{i}{2^i} = \sum^n_{k=1} \sum^n_{i=k} \frac{1}{2^i}$, $\sum^n_{i=k} \frac{1}{2^i} = \sum^n_{i=0} \frac{1}{2^i} - \sum^{k-1}_{i=0} \frac{1}{2^i}$
By **Proposition 3.5** on page 121,
$\sum^n_{i=0} \frac{1}{2^i} - \sum^{k-1}_{i=0} \frac{1}{2^i} = \frac{\frac{1}{2}^{n+1}-\frac{1}{2}^{k}}{\frac{1}{2}-1} = \frac{1}{2}^{k-1}-\frac{1}{2}^{n} < \frac{1}{2}^{k-1}$
Then
$\sum^n_{k=1} \sum^n_{i=k} \frac{1}{2^i} < \sum^n_{k=1} \frac{1}{2}^{k-1} = \sum^{n-1}_{k=0} \frac{1}{2}^{k}$
Apply **Proposition 3.5** on page 121 again,
$\sum^n_{k=1} \sum^n_{i=k} \frac{1}{2^i} < \frac{\frac{1}{2}^n - 1}{\frac{1}{2}-1} = 2 - \frac{1}{2}^{n-1} < 2$

Hence, $\sum^n_{i=1} \frac{i}{2^i} < 2$.

Awareness of a non-optimal algorithm will sometimes help you write a proof.
