If $d(n)$ is $O(f(n))$ then $\exists$ $c_d > 0$ and $n_{0d} > 1$ such that $d(n) \leq c_df(n)$ for $n \geq n_{0d}$.
Likewise, if $e(n)$ is $O(g(n))$ then $\exists$ $c_e > 0$ and $n_{0e} > 1$ such that $e(n) \leq c_eg(n)$ for
$n \geq n_{0e}$.  However, $-e(n) \geq -c_eg(n)$ for $n \geq n_{0e}$ Therefore, $d(n) - e(n) \leq c_df(n) - c_eg(n)$
for $n \geq \max(n_{0d}, n_{0e})$ is **not necessarily** true. Hence, $d(n) - e(n)$ is **not necessarily**
$O(f(n) - g(n))$.
