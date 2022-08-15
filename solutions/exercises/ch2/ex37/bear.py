from random import random

from solutions.exercises.ch2.ex37.animal import Animal


class Bear(Animal):
    def __init__(self):
        self._rank = 2
        super().__init__()

    def __str__(self):
        return "B"
