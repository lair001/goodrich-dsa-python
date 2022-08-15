from random import random


class Animal:
    _gender: bool
    _strength: float
    _rank: int

    def __init__(self):
        self._gender = random() < 0.5
        self._strength = random()

    def get_gender(self) -> str:
        return "M" if self._gender else "F"

    def get_strength(self) -> float:
        return self._strength * 255

    def get_rank(self) -> int:
        return self._rank

    def make_move(self) -> int:
        rand = random()
        if rand < 0.334:
            return 0
        elif rand < 0.667:
            return -1
        else:
            return 1
