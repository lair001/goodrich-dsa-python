When Bob wants to send Alice a message $M$ on the Internet, he breaks $M$
into $n$ ***data packets***, numbers the packets consecutively, and injects them
into the network. When the packets arrive at Alice’s computer, they may
be out of order, so Alice must assemble the sequence of $n$ packets in order
before she can be sure she has the entire message. Describe an efficient
scheme for Alice to do this, assuming that she knows the value of $n$. What
is the running time of this algorithm?