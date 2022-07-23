The Vector class of Section 2.3.3 provides a constructor that takes an
integer d, and produces a d-dimensional vector with all coordinates
equal to 0. Another convenient form for creating a new vector would be
to send the constructor a parameter that is some iterable type
representing a sequence of numbers, and to create a vector with
dimension equal to the length of that sequence and coordinates equal to
the sequence values. For example, Vector(\[4, 7, 5\]) would produce a
three-dimensional vector with coordinates <4, 7, 5>. Modify the
constructor so that either of these forms is acceptable; that is, if a
single integer is sent, it produces a vector of that dimension with all
zeros, but if a sequence of numbers is provided, it produces a vector
with coordinates based on that sequence.