The actual parameter sent by the caller is a list.
The statement `data[j] *= factor` expands out to
`data[j] = data[j] * factor`.  I.e. on each iteration,
`data[j] * factor` is evaluated and assigned to data[j].