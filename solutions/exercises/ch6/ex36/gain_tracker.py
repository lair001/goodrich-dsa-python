from solutions.vendor.ch06.array_queue import ArrayQueue


class GainTracker:

    _shares: ArrayQueue
    _gain_in_cents: int

    def __init__(self):
        self._shares = ArrayQueue()
        self._gain_in_cents = 0

    def buy(self, shares: int, price_in_cents: int):
        self._shares.enqueue([shares, price_in_cents])

    def sell(self, shares: int, price_in_cents: int):
        while shares > 0:
            first = self._shares.first()
            self._gain_in_cents += min(shares, first[0]) * (price_in_cents - first[1])
            tmp = first[0]
            first[0] -= shares
            shares -= tmp
            if first[0] <= 0:
                self._shares.dequeue()

    def get_gains_in_cents(self):
        return self._gain_in_cents

