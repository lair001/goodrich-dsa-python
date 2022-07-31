If $d(n)$ is $O(f(n)+g(n))$ then $\exists$ $c > 0$ and $n_{0} \geq 1$ such that $d(n) \leq c(f(n)+g(n))$ for $n \geq n_{0}$.
It follows that $d(n) \leq c(f(n)+g(n)) \leq 2c\max(f(n),g(n))$ for n $\geq n_{0}$.

Now let's go the other way around. If $d(n)$ is $O(\max(f(n),g(n)))$ then $\exists$ $c > 0$ and $n_{0} > 1$ such that
$d(n) \leq c\max(f(n)+g(n))$ for $n \geq n_{0}$. It follows that $d(n) \leq c\max(f(n),g(n)) \leq c(f(n)+g(n))$ for
$n \geq n_{0}$ (assuming $f(n) \geq 0$ and $g(n) \geq 0$ for $n \geq n_{0}$).

Hence, $O(\max(f(n),g(n)))$ is $O(f(n)+g(n))$.
