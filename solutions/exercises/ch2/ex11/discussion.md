List's \_\_add\_\_ method only accepts another list as an argument, and
it is concatenation rather than vector addition anyway.  To solve this
issue, simply define an \_\_radd\_\_ for Vector that behaves just like
Vector's \_\_add\_\_ method.