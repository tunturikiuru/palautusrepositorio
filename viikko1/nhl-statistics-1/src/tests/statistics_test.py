import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_find_player(self):
        player = self.stats.search("Yzerman")
        self.assertEqual(str(player), str(Player("Yzerman", "DET", 42, 56)))

    def test_player_doesnt_exist(self):
        player = self.stats.search("Markkanen")
        self.assertAlmostEqual(player, None)

    def test_team_search(self):
        players = self.stats.team("EDM")
        players = [str(player) for player in players]
        self.assertAlmostEqual(players, [str(Player("Semenko", "EDM", 4, 12)), str(Player("Kurri",   "EDM", 37, 53)), str(Player("Gretzky", "EDM", 35, 89))])

    def test_best_players(self):
        top = self.stats.top(1)
        top = [str(player) for player in top]
        self.assertAlmostEqual(top, [str(Player("Gretzky", "EDM", 35, 89)), str(Player("Lemieux", "PIT", 45, 54))])

    def test_top_players_by_points(self):
        top = self.stats.top(1, SortBy.POINTS)
        top = [str(player) for player in top]
        self.assertAlmostEqual(top, [str(Player("Gretzky", "EDM", 35, 89)), str(Player("Lemieux", "PIT", 45, 54))])

    def test_top_players_by_goals(self):
        top = self.stats.top(1, SortBy.GOALS)
        top = [str(player) for player in top]
        self.assertAlmostEqual(top, [str(Player("Lemieux", "PIT", 45, 54)), str(Player("Yzerman", "DET", 42, 56))])

    def test_top_player_by_assists(self):
        top = self.stats.top(1, SortBy.ASSISTS)
        top = [str(player) for player in top]
        self.assertAlmostEqual(top, [str(Player("Gretzky", "EDM", 35, 89)), str(Player("Yzerman", "DET", 42, 56))])

