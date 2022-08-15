from solutions.vendor.ch06.array_stack import ArrayStack
from solutions.vendor.ch06.empty import Empty


class StackDeque:
    _left_stack: ArrayStack
    _right_stack: ArrayStack

    def __init__(self):
        self._left_stack = ArrayStack()
        self._right_stack = ArrayStack()

    def __len__(self):
        return len(self._left_stack) + len(self._right_stack)

    def is_empty(self):
        return self._left_stack.is_empty() and self._right_stack.is_empty()

    def add_first(self, e):
        self._left_stack.push(e)

    def add_last(self, e):
        self._right_stack.push(e)

    def _transfer(self, _from: ArrayStack, _to: ArrayStack):
        for _ in range(len(_from)):
            _to.push(_from.pop())

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty!")
        if self._left_stack.is_empty():
            if len(self) == 1:
                return self._right_stack.top()
            else:
                self._transfer(self._right_stack, self._left_stack)
        return self._left_stack.top()

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty!")
        if self._left_stack.is_empty():
            if len(self) == 1:
                return self._right_stack.pop()
            else:
                self._transfer(self._right_stack, self._left_stack)
        return self._left_stack.pop()

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty!")
        if self._right_stack.is_empty():
            if len(self) == 1:
                return self._left_stack.top()
            else:
                self._transfer(self._left_stack, self._right_stack)
        return self._right_stack.top()

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty!")
        if self._right_stack.is_empty():
            if len(self) == 1:
                return self._left_stack.pop()
            else:
                self._transfer(self._left_stack, self._right_stack)
        return self._right_stack.pop()

    def __str__(self):
        if self.is_empty():
            return "[]"
        elif self._right_stack.is_empty():
            return "[{}]".format(self._left_stack.__str__().lstrip("[").rstrip("]")[::-1])
        elif self._left_stack.is_empty():
            return self._right_stack.__str__()
        else:
            return "[{}, {}".format(self._left_stack.__str__().lstrip("[").rstrip("]")[::-1],
                                   self._right_stack.__str__().lstrip("["))
