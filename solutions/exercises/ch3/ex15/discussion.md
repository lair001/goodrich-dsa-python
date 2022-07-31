If $f(n)$ is $O(g(n))$ then $\exists$ $c > 0$ and $n_0 \geq 1$ such that $f(n) \leq cg(n)$ for $n \geq n_0$. Therefore,
$g(n) \geq \frac{1}{c}f(n)$ for $n \geq n_0$.

Now let us go the other way. If $g(n)$ is $Ω(f(n))$ then $\exists$ $c > 0$ and $n_0 \geq 1$ such that
$g(n) \geq cf(n)$ for $n \geq n_0$. Therefore, $f(n) \leq \frac{1}{c}g(n)$ for $n \geq n_0$.

Hence, $f(n)$ is $O(g(n))$ if and only if $g(n)$ is $Ω(f(n))$.
