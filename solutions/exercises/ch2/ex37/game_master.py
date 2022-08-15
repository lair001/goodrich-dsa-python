import random
from typing import Mapping, Type, ClassVar

from solutions.exercises.ch2.ex37.bear import Bear
from solutions.exercises.ch2.ex37.fish import Fish
from solutions.exercises.ch2.ex37.animal import Animal


class GameMaster:
    BoardPiece = Type[Fish | Bear | None]
    _board: list[BoardPiece]
    _counts: dict[BoardPiece, int]
    _fish: int
    _bears: int
    _remaining: list[int]

    def __init__(self, size: int, fish: int, bears: int):
        self._board = [None] * size
        self._fish = fish
        self._bears = bears
        self._remaining = [i for i in range(len(self._board))]
        self._counts = {
            Fish: self._fish,
            Bear: self._bears
        }

    def _setup_board(self):
        """Initialize board before a game."""
        fish = self._fish
        bears = self._bears
        while fish > 0 or bears > 0:
            rand = random.choice(self._remaining)
            self._remaining.remove(rand)
            if fish > 0:
                self._board[rand] = Fish()
                fish -= 1
            else:
                self._board[rand] = Bear()
                bears -= 1
        self._show_board()

    def _teardown_board(self):
        """Teardown the board after a game."""
        for i in range(len(self._board)):
            if self._board[i] is not None:
                self._board[i] = None
        self._remaining = [i for i in range(len(self._board))]
        self._counts[Fish] = self._fish
        self._counts[Bear] = self._bears

    def __str__(self):
        result = ["|"] * (2 * len(self._board) + 1)
        for i in range(len(self._board)):
            result[2*i + 1] = " " if self._board[i] is None else self._board[i].__str__()
        return " ".join(result)

    def _show_board(self):
        """Print the current state of the board."""
        print(self)

    def _resolve_battle(self, curr: Animal, other: Animal):
        if curr.get_rank() == other.get_rank():
            if curr.get_strength() == other.get_strength():
                return None
            else:
                return curr if curr.get_strength() > other.get_strength() else other
        elif curr.get_rank() > other.get_rank():
            return curr
        else:
            return other

    def officiate_game(self):
        """Run the simulation."""
        self._setup_board()

        while self._counts.get(Fish) > 0 and self._counts.get(Bear) > 1:
            for i in range(len(self._board)):
                curr: Animal = self._board[i]
                if curr is not None:
                    move: int = curr.make_move()
                    if move == 0 or i + move < 0 or i + move == len(self._board):
                        continue
                    else:
                        other: Animal = self._board[i + move]
                        if type(curr) == type(other) and curr.get_gender() != other.get_gender():
                            if len(self._remaining) > 0:
                                j = random.choice(self._remaining)
                                self._remaining.remove(j)
                                self._board[j] = type(curr)()
                                self._counts[type(curr)] = self._counts[type(curr)] + 1
                        else:
                            self._board[i] = None
                            self._remaining.append(i)
                            if other is None:
                                self._board[i + move] = curr
                                self._remaining.remove(i + move)
                            else:
                                winner = self._resolve_battle(curr, other)
                                if winner is None:
                                    self._board[i + move] = None
                                    self._counts[type(curr)] = self._counts[type(curr)] - 2
                                    self._remaining.append(i + move)
                                elif winner is curr:
                                    self._board[i + move] = curr
                                    self._counts[type(other)] = self._counts[type(other)] - 1
                                elif winner is other:
                                    self._counts[type(curr)] = self._counts[type(curr)] - 1
            self._show_board()

        self._teardown_board()
