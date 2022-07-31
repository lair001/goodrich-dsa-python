If $d(n)$ is $O(f(n))$ then $\exists$ $c_d > 0$ and $n_{0d} \geq 1$ such that $d(n) \leq c_df(n)$ for $n \geq n_{0d}$.
Likewise, if $f(n)$ is $O(g(n))$ then $\exists$ $c_f > 0$ and $n_{0f} \geq 1$ such that $f(n) \leq c_fg(n)$ for
$n \geq n_{0f}$. Therefore, $d(n) \leq c_df(n) \leq c_d c_f g(n)$ for $n \geq \max(n_{0d},n_{0f})$.
Hence, $d(n)$ is $O(g(n))$.
