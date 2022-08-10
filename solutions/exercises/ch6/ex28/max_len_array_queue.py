from solutions.exercises.ch6.ex16.full import Full
from solutions.vendor.ch06.array_queue import ArrayQueue as Ch6ArrayQueue


class MaxLenArrayQueue(Ch6ArrayQueue):
    def __init__(self, maxlen=None):
        self._maxlen = maxlen
        self._data = [None] * (Ch6ArrayQueue.DEFAULT_CAPACITY if maxlen is None else maxlen)
        self._size = 0
        self._front = 0

    def enqueue(self, e):
        if len(self) == self._maxlen:
            raise Full("Can't enqueue onto a full queue!")
        super().enqueue(e)

    # The vendor ArrayQueue dequeue method never shrinks the data list, so we should be done!
