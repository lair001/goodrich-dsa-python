A useful operation in databases is the natural join. If we view a database
as a list of ordered pairs of objects, then the natural join of databases $A$
and $B$ is the list of all ordered triples $(x,y,z)$ such that the pair $(x,y)$ is in
A and the pair $(y,z)$ is in $B$. Describe and analyze an efficient algorithm
for computing the natural join of a list $A$ of $n$ pairs and a list $B$ of $m$ pairs.