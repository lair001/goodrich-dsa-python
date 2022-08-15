\_\_len\_\_ and is_empty run in $O(1)$ time.

add_first and add_last run in amortized $O(1)$ time.

Unfortunately, first, last, delete_first, and delete_last run in $O(n)$ time since it is possible to force
a transfer between stacks on each operation by alternating between the ends of queue after one of the stacks
has been exhausted. However, if we were allowed to use a third instance variable of either a queue or a stack,
it would be possible to obtain amortized $O(1)$ time.