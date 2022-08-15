from solutions.vendor.ch06.array_stack import ArrayStack
from solutions.vendor.ch06.empty import Empty


class StackQueue:
    _enqueue_stack: ArrayStack
    _dequeue_stack: ArrayStack

    def __init__(self):
        self._enqueue_stack = ArrayStack()
        self._dequeue_stack = ArrayStack()

    def __len__(self):
        return len(self._enqueue_stack) + len(self._dequeue_stack)

    def is_empty(self):
        return self._enqueue_stack.is_empty() and self._dequeue_stack.is_empty()

    def enqueue(self, e):
        self._enqueue_stack.push(e)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        if self._dequeue_stack.is_empty():
            while not self._enqueue_stack.is_empty():
                self._dequeue_stack.push(self._dequeue_stack.pop())
        return self._dequeue_stack.pop()

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        if self._dequeue_stack.is_empty():
            while not self._enqueue_stack.is_empty():
                self._dequeue_stack.push(self._enqueue_stack.pop())
        return self._dequeue_stack.top()

    def __str__(self):
        if self.is_empty():
            return "[]"
        elif self._enqueue_stack.is_empty():
            return self._dequeue_stack.__str__()
        elif self._dequeue_stack.is_empty():
            return "[{}]".format(self._enqueue_stack.__str__().lstrip("[").rstrip("]")[::-1])
        else:
            return "{}, {}]".format(self._dequeue_stack.__str__().rstrip("]"),
                                    self._enqueue_stack.__str__().lstrip("[").rstrip("]")[::-1])
