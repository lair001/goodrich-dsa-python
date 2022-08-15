from random import random

from solutions.exercises.ch2.ex37.animal import Animal


class Fish(Animal):
    def __init__(self):
        self._rank = 1
        super().__init__()

    def __str__(self) -> str:
        return "F"
