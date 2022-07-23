This implementation of scale does not work.  On each
iteration, the value of an element of data is assigned
into a local variable val. val * factor is evaluated and
assigned to val. I.e. no assignments are made to the
elements of data.

On any given iteration, data[j] and val point to
different memory addresses.
