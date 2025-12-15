# tests/test_nba.py
import unittest
from models.player_metric import ShootingStat, ScoringStat, DefenseStat, PointGuardAssists, BigManRebounds

class TestMetrics(unittest.TestCase):
    def test_shooting_stat(self):
        self.assertEqual(ShootingStat(65).rate(), "Excellent-5")
        self.assertEqual(ShootingStat(25).rate(), "Bad-2")

    def test_scoring_stat(self):
        self.assertEqual(ScoringStat(30).rate(), "Good-4")
        self.assertEqual(ScoringStat(5).rate(), "Terrible-1")

    def test_defense_stat(self):
        self.assertEqual(DefenseStat(4).rate(), "Excellent-5")
        self.assertEqual(DefenseStat(0.2).rate(), "Terrible-1")

    def test_assists_pg(self):
        self.assertEqual(PointGuardAssists("Chris Paul", 10).evaluate(), ("Good", 4))

    def test_rebounds_bigman(self):
        self.assertEqual(BigManRebounds("Nikola Jokic", 15).evaluate(), ("Excellent", 5))
