from solutions.vendor.ch06.array_queue import ArrayQueue as Ch6ArrayQueue
from solutions.vendor.ch06.empty import Empty


class RotatableArrayQueue(Ch6ArrayQueue):
    def rotate(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        e = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        avail = (self._front + self._size - 1) % len(self._data)
        self._data[avail] = e
