Our implementation of insert for the DynamicArray class, as given in
Code Fragment 5.5, has the following inefficiency. In the case when a resize occurs, the resize operation takes time to
copy all the elements from an old array to a new array, and then the subsequent loop in the body of
insert shifts many of those elements. Give an improved implementation
of the insert method, so that, in the case of a resize, the elements are
shifted into their final position during that operation, thereby avoiding the
subsequent shifting.