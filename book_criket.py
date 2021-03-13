from abc import ABC
from random import randint


class NumberGenerator(ABC):
    def generate_numbers(self, size):
        pass


class RandomNumberGenerator(NumberGenerator):
    def generate_numbers(self, size):
        for counter in range(size):
            yield randint(0, 10)


class BookCricket:
    def __init__(self, number_generator):
        self._scores = None
        self._target = None
        self.number_generator = number_generator

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value

    def play(self):
        self.generate_scores()
        return "The player has won" if self.has_won() else "The player has lost"

    def generate_scores(self):
        self._scores = self.number_generator.generate_numbers(6)

    def has_won(self):
        return sum(self._scores) >= self._target


if __name__ == '__main__':
    bk = BookCricket(RandomNumberGenerator())
    bk.target = 10
    print(bk.play())
