from abc import ABC
from random import randint


class NumberGenerator(ABC):
    def generate_number(self):
        pass


class RandomNumberGenerator(NumberGenerator):
    def generate_number(self):
        return randint(0, 10)


class Player:
    def __init__(self, name, number_generator):
        self.name = name
        self.number_generator = number_generator

    def generate_number(self):
        return self.number_generator.generate_number()


class Playable(ABC):
    def play(self):
        pass


class CricketGame(Playable):
    def __init__(self, first_player, second_player, overs, target):
        self.first_player = first_player
        self.second_player = second_player
        self.overs = overs
        self.first_player_score = 0
        self.target = target

    def play(self):
        for i in range(self.overs * 6):
            first = self.first_player.generate_number()
            second = self.second_player.generate_number()
            print(f'{self.first_player.name}: {first}')
            print(f'{self.second_player.name}: {second}')
            if first == second:
                print(f'{self.first_player.name} has Lost the game')
                return
            self.first_player_score += first
            if self.first_player_score >= self.target:
                print(f"{self.first_player.name} has won")
                return
        print(f"{self.first_player.name} has lost")


if __name__ == '__main__':
    bats_man = Player("Bats man", RandomNumberGenerator())
    bowler = Player("Bowler", RandomNumberGenerator())
    game = CricketGame(bats_man, bowler, 2, 30)
    game.play()
