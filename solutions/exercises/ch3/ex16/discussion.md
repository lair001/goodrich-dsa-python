Suppose $p(n)$ is a polynomial in $n$ of degree $d$. The $\log_2 p(n) = \log_2(a_d n^d + ... + a_2 n^2 + a_1 n + a_0)$
$\leq \log_2 (\max(a_d, ..., a_2, a_1, a_0)(d+1)n^d)$ for large n. Take $a = log_2(\max(a_d, ..., a_2, a_1, a_0)(d+1))$
Then $\log_2 (\max(a_d, ..., a_2, a_1, a_0)(d+1)n^d) = a + d\log_2(n)$. Take $n_0 = 2$ and $c = a + d$. Then
$\log_2 p(n) \leq (a + d)log_2(n)$ for $n \geq 2$. Hence, $\log p(n)$ is $O(\log n)$.

These arguments break down if all the coefficients $a_n, ..., a_0$ of $p(n)$ are negative, but such a polynomial would
be $< 0$ for $n > 0$. This is nonsensical if the polynomial represents the runtime of an algorithm for a problem of
size $n$.
