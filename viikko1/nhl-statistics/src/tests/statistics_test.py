import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_with_correct_player(self):
        player = self.stats.search('Yzerman')
        self.assertEqual(player.goals, 42)

    def test_search_without_correct_player(self):
        player = self.stats.search('Yserman')
        self.assertEqual(player, None)

    def test_search_by_team(self):
        team = self.stats.team('EDM')
        self.assertEqual(len(team), 3)

    def test_search_top_players(self):
        top = self.stats.top(2)
        self.assertEqual(str(top[1]), 'Lemieux PIT 45 + 54 = 99')

    def test_search_top_players_by_points(self):
        sortby = SortBy.POINTS
        top = self.stats.top(2, sortby)
        self.assertEqual(str(top[1]), 'Lemieux PIT 45 + 54 = 99')

    def test_search_top_players_by_goals(self):
        sortby = SortBy.GOALS
        top = self.stats.top(2, sortby)
        self.assertEqual(str(top[1]), 'Yzerman DET 42 + 56 = 98')

    def test_search_top_players_by_assists(self):
        sortby = SortBy.ASSISTS
        top = self.stats.top(2, sortby)
        self.assertEqual(str(top[1]), 'Yzerman DET 42 + 56 = 98')