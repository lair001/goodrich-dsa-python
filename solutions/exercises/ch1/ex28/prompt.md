The _**p-norm**_ of a vector <img src="/solutions/exercises/C/ch1/ex28/tex/0ee98ff05a88e05a465be9842fc6e97c.svg?invert_in_darkmode&sanitize=true" align=middle width=139.26359204999997pt height=24.65753399999998pt/> in _n_-dimensional space is defined as  
<p align="center"> <img src="/solutions/exercises/C/ch1/ex28/tex/a88ab67d88d4d6a139d0153a83ee6e15.svg?invert_in_darkmode&sanitize=true" align=middle width=189.13327619999998pt height=29.67601559999999pt/>. </p>

For the special case of _p_ = 2, this results in the traditional
_**Euclidean norm**_, which represents the length of the vector. For
example, the Euclidean norm of a two-dimensional with coordinates
(4, 3) has a Euclidean norm of
<img src="/solutions/exercises/C/ch1/ex28/tex/536c48fd312edf4590d5f80642d850bd.svg?invert_in_darkmode&sanitize=true" align=middle width=227.5338285pt height=28.712280299999996pt/>.
Give an implementation of a function named norm such that norm(v, p)
returns the p-norm value of _v_ and norm(v) returns the Euclidean norm
of _v_. You may assume that _v_ is a list of numbers.