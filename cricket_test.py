import unittest

from cricket import Player, RandomNumberGenerator, Hitter, CricketGame, Defence, NormalShotCompare, LazyShotCompare


class CricketTestClass(unittest.TestCase):
    def test_game_play_logic(self):
        bats_man = Player("Batsman", RandomNumberGenerator())
        bowler = Player("Bowler", Hitter())
        shot_compare = NormalShotCompare()
        game = CricketGame(bats_man, bowler, 2, 10, shot_compare)
        game.play()
        self.assertTrue(game.has_won(), bats_man.get_total_score() >= 10)

    def test_total_score_of_player(self):
        batsman = Player("Batsman", RandomNumberGenerator())
        expected = 0
        for i in range(6):
            number = batsman.get_score()
            expected += number
        self.assertEqual(expected, batsman.get_total_score())

    def test_normal_batsman_hit(self):
        batsman = Player("Batsman", RandomNumberGenerator())
        self.assertTrue(batsman.get_score() in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_hitter_hits_accordingly(self):
        hitter = Player("Hitter", Hitter())
        score = hitter.get_score()
        self.assertTrue(score in [0, 4, 6] and score not in [1, 2, 3, 5, 7, 8, 9, 10])

    def test_defence_hits_accordingly(self):
        defence = Player("Defence", Defence())
        score = defence.get_score()
        self.assertTrue(score in [0, 1, 2, 3] and score not in [4, 5, 6, 7, 8, 9, 10])

    def test_compare_strategy(self):
        shot_compare = NormalShotCompare()
        lazy_shot_compare = LazyShotCompare()
        self.assertTrue(shot_compare.compare(5, 5))
        self.assertTrue(not lazy_shot_compare.compare(4, 9))

    if __name__ == '__main__':
        unittest.main()
