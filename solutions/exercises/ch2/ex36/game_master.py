import random

from solutions.exercises.ch2.ex36.bear import Bear
from solutions.exercises.ch2.ex36.fish import Fish


class GameMaster:
    _board: list
    _fish: int
    _bears: int
    _remaining: list[int]

    def __init__(self, size: int, fish: int, bears: int):
        self._board = [None] * size
        self._fish = fish
        self._bears = bears
        self._remaining = [i for i in range(len(self._board))]

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

    def __str__(self):
        result = ["|"] * (2 * len(self._board) + 1)
        for i in range(len(self._board)):
            result[2*i + 1] = " " if self._board[i] is None else self._board[i].__str__()
        return " ".join(result)

    def _show_board(self):
        """Print the current state of the board."""
        print(self)

    def officiate_game(self):
        """Run the simulation."""
        self._setup_board()

        fish = self._fish
        bears = self._bears
        while fish > 0 and bears > 0:
            for i in range(len(self._board)):
                curr = self._board[i]
                if curr is not None:
                    move = curr.make_move()
                    if move == 0 or i + move < 0 or i + move == len(self._board):
                        continue
                    else:
                        other = self._board[i + move]
                        if type(curr) == type(other):
                            if len(self._remaining) > 0:
                                j = random.choice(self._remaining)
                                self._remaining.remove(j)
                                self._board[j] = type(curr)()
                                if type(curr) == Fish:
                                    fish += 1
                                else:
                                    bears += 1
                        else:
                            if type(curr) == Bear or other is None:
                                self._board[i + move] = curr
                            self._board[i] = None
                            self._remaining.append(i)
                            if other is not None:
                                fish -= 1
                            else:
                                self._remaining.remove(i + move)
            self._show_board()

        self._teardown_board()
