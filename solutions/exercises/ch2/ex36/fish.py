from random import random


class Fish:
    def __str__(self) -> str:
        return "F"

    def make_move(self) -> int:
        rand = random()
        if rand < 0.334:
            return 0
        elif rand < 0.667:
            return -1
        else:
            return 1

