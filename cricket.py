from abc import ABC
from random import randint


class NumberGenerator(ABC):
    def get_score(self):
        pass


class RandomNumberGenerator(NumberGenerator):
    def get_score(self):
        return randint(0, 10)


class Hitter(NumberGenerator):
    def get_score(self):
        array = [0, 4, 6]
        return array[randint(0, 2)]


class Defence(NumberGenerator):
    def get_score(self):
        array = [0, 1, 2, 3]
        return array[randint(0, 3)]


class Player:
    def __init__(self, name, number_generator):
        self.name = name
        self.number_generator = number_generator
        self.scores = []
        self.total_score = 0

    def get_score(self):
        score = self.number_generator.get_score()
        self.total_score += score
        self.scores.append(score)
        return score

    def get_total_score(self):
        return self.total_score

    def get_scores(self):
        return self.scores


class Playable(ABC):
    def play(self):
        pass

    def has_won(self):
        pass


class ShotCompare(ABC):
    def compare(self, a, b):
        pass


class NormalShotCompare(ShotCompare):
    def compare(self, a, b):
        return a == b


class LazyShotCompare(ShotCompare):
    def compare(self, a, b):
        return False


class CricketGame(Playable):
    def __init__(self, first_player, second_player, overs, target, shot_compare):
        self.batsman = first_player
        self.bowler = second_player
        self.overs = overs
        self.batsman_score = 0
        self.target = target
        self.iterations = 0
        self.shot_compare = shot_compare

    def play(self):
        for i in range(self.overs * 6):
            first = self.batsman.get_score()
            second = self.bowler.get_score()
            print(f'{self.batsman.name}: {first}')
            print(f'{self.bowler.name}: {second}')
            self.iterations += 1
            # print(type())
            # print(Defence)
            # print
            if self.shot_compare.compare(first, second):
                print(f'{self.batsman.name} has Lost the game')
                return
            self.batsman_score += first
            if self.has_won():
                print(f"{self.batsman.name} has won")
                return
        print(f"{self.batsman.name} has lost")

    def has_won(self):
        return self.batsman.total_score >= self.target if self.batsman.scores[-1] != self.bowler.scores[-1] \
            else self.batsman.total_score - self.batsman.scores[-1]


if __name__ == '__main__':
    bats_man = Player("Defence", Defence())
    bowler = Player("Bowler", RandomNumberGenerator())
    game = CricketGame(bats_man, bowler, 2, 10, LazyShotCompare())
    game.play()
