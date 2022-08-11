In certain applications of the queue ADT, it is common to repeatedly
dequeue an element, process it in some way, and then immediately enqueue the same element. Modify the ArrayQueue
implementation to include a rotate( ) method that has semantics identical to the combination, Q.enqueue(Q.dequeue( )).
However, your implementation should be more efficient than making two separate calls (for example, because there is no
need to modify size).