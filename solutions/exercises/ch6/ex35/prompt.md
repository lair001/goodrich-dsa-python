The introduction of Section 6.1 notes that stacks are often used to provide
“undo” support in applications like a Web browser or text editor. While
support for undo can be implemented with an unbounded stack, many
applications provide only ***limited*** support for such an undo history, with a
fixed-capacity stack. When push is invoked with the stack at full capacity,
rather than throwing a Full exception (as described in Exercise C-6.16),
a more typical semantic is to accept the pushed element at the top while
“leaking” the oldest element from the bottom of the stack to make room.
Give an implementation of such a LeakyStack abstraction, using a circular
array with appropriate storage capacity. This class should have a public
interface similar to the bounded-capacity stack in Exercise C-6.16, but
with the desired leaky semantics when full.