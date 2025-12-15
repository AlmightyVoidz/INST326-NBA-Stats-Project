# tests/test_nba.py
import unittest
from src.models.player_metric import (
    ShootingStat,
    ScoringStat,
    DefenseStat,
    PointGuardAssists,
    CenterAssists,
    GuardRebounds,
    BigManRebounds
)
from src.evaluator.evaluator import Evaluator
from src.io.importer import import_csv
from src.io.exporter import export_csv
from src.io.persistence import save_data, load_data
from pathlib import Path
import os

class TestUnitMetrics(unittest.TestCase):
    """Unit tests for individual metrics"""

    def test_shooting_stat(self):
        self.assertEqual(ShootingStat(65).rate(), "Excellent-5")
        self.assertEqual(ShootingStat(25).rate(), "Bad-2")

    def test_scoring_stat(self):
        self.assertEqual(ScoringStat(30).rate(), "Good-4")
        self.assertEqual(ScoringStat(5).rate(), "Terrible-1")

    def test_defense_stat(self):
        self.assertEqual(DefenseStat(4).rate(), "Excellent-5")
        self.assertEqual(DefenseStat(0.2).rate(), "Terrible-1")

    def test_assists_metrics(self):
        self.assertEqual(PointGuardAssists("Chris Paul", 10).evaluate(), ("Good", 4))
        self.assertEqual(CenterAssists("Nikola Jokic", 5).evaluate(), ("OK", 3))

    def test_rebounds_metrics(self):
        self.assertEqual(BigManRebounds("Nikola Jokic", 15).evaluate(), ("Excellent", 5))
        self.assertEqual(GuardRebounds("Klay Thompson", 2).evaluate(), ("Bad", 2))


class TestIntegrationEvaluator(unittest.TestCase):
    """Integration tests: Evaluator with multiple metrics"""

    def test_evaluator_run_all(self):
        evaluator = Evaluator()
        evaluator.add_metric(PointGuardAssists("Chris Paul", 9))
        evaluator.add_metric(BigManRebounds("Nikola Jokic", 12))
        results = evaluator.run_all()

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["player"], "Chris Paul")
        self.assertEqual(results[1]["player"], "Nikola Jokic")
        self.assertEqual(results[0]["rating"], "Good")
        self.assertEqual(results[1]["rating"], "Good")


class TestSystemIO(unittest.TestCase):
    """System tests: Import, Export, and Persistence"""

    def setUp(self):
        # Create a temp file for export
        self.test_file = "data/test_export.csv"
        self.test_json = "data/nba_data.json"

    def tearDown(self):
        # Clean up temp files
        if Path(self.test_file).exists():
            os.remove(self.test_file)
        if Path(self.test_json).exists():
            os.remove(self.test_json)

    def test_import_csv(self):
        data = import_csv("data/sample_nba.csv")
        self.assertTrue(len(data) > 0)
        self.assertIn("Name", data[0])
        self.assertIn("Assists", data[0])

    def test_export_csv(self):
        export_csv(self.test_file, [{"player": "Test Player", "metric": "PG", "rating": "Good", "score": 4}])
        self.assertTrue(Path(self.test_file).exists())

    def test_save_load_data(self):
        test_data = [{"player": "Test Player", "metric": "PG", "rating": "Good", "score": 4}]
        save_data(test_data)
        loaded = load_data()
        self.assertEqual(loaded, test_data)


if __name__ == "__main__":
    unittest.main()
