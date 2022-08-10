from solutions.exercises.ch6.ex16.full import Full
from solutions.vendor.ch06.array_stack import ArrayStack as Ch6ArrayStack


class MaxLenArrayStack(Ch6ArrayStack):
    def __init__(self, maxlen=None):
        self._maxlen = maxlen
        super().__init__()

    def push(self, e):
        if len(self) == self._maxlen:
            raise Full("Can't push onto a full stack!")
        super().push(e)
