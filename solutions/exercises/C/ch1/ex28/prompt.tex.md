The _**p-norm**_ of a vector $v = (v_1 + v_2, ..., v_n)$ in _n_-dimensional space is defined as  
<p align="center"> $||v|| = \sqrt[p]{v_1^p + v_2^p + ... + v_2^p}$. </p>

For the special case of _p_ = 2, this results in the traditional
_**Euclidean norm**_, which represents the length of the vector. For
example, the Euclidean norm of a two-dimensional with coordinates
(4, 3) has a Euclidean norm of
$\sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5$.
Give an implementation of a function named norm such that norm(v, p)
returns the p-norm value of _v_ and norm(v) returns the Euclidean norm
of _v_. You may assume that _v_ is a list of numbers.