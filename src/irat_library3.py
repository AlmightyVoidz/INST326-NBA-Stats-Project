#Project 3

#SHOOTING/SCORING

from abc import ABC, abstractmethod

class AbstractStat(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def rate(self):
        pass


class ShootingStat(AbstractStat):
    def rate(self):
        if self.value >= 60:
            return "Excellent-5"
        elif self.value >= 50:
            return "Good-4"
        elif self.value >= 40:
            return "OK-3"
        elif self.value >= 30:
            return "Bad-2"
        else:
            return "Terrible-1"


class ScoringStat(AbstractStat):
    def rate(self):
        if self.value >= 35:
            return "Excellent-5"
        elif self.value >= 25:
            return "Good-4"
        elif self.value >= 15:
            return "OK-3"
        elif self.value >= 8:
            return "Bad-2"
        else:
            return "Terrible-1"


class DefenseStat(AbstractStat):
    def rate(self):
        if self.value >= 3.5:
            return "Excellent-5"
        elif self.value >= 2:
            return "Good-4"
        elif self.value >= 1:
            return "OK-3"
        elif self.value >= 0.5:
            return "Bad-2"
        else:
            return "Terrible-1"


class NBAAnalyzer:
    def __init__(self):
        self.stats = []

    def add_stat(self, stat):
        self.stats.append(stat)

    def analyze(self):
        results = []
        for s in self.stats:
            results.append(s.rate())
        return results


def main():
    analyzer = NBAAnalyzer()

    print("NBA STAT ANALYZER")
    print("1 = Shooting Percentage (%)")
    print("2 = Points Per Game")
    print("3 = Blocks/Steals Per Game")

    choice = int(input("Choose stat type: "))
    value = float(input("Enter stat value: "))

    if choice == 1:
        analyzer.add_stat(ShootingStat(value))
    elif choice == 2:
        analyzer.add_stat(ScoringStat(value))
    elif choice == 3:
        analyzer.add_stat(DefenseStat(value))
    else:
        print("Invalid option.")
        return

    results = analyzer.analyze()
    print("Rating:", results[0])


if __name__ == "__main__":
    main()

#ASSISTS

# src/player_metric.py
from abc import ABC, abstractmethod

class PlayerMetric(ABC):
    """
    Abstract base class for all NBA player metrics.
    Defines a standard interface for evaluating statistical performance.
    """

    def __init__(self, player_name, value):
        if not isinstance(player_name, str) or not player_name.strip():
            raise ValueError("Player name must be a non-empty string.")

        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Metric value must be a non-negative number.")

        self._player_name = player_name
        self._value = value

    @property
    def player_name(self):
        return self._player_name

    @property
    def value(self):
        return self._value

    @abstractmethod
    def evaluate(self):
        """
        Return a rating based on the metric value.
        Subclasses must implement this.
        """
        pass

    def __str__(self):
        return f"{self.player_name}: {self.value}"

# src/assists_metric.py
from player_metric import PlayerMetric

class AssistsMetric(PlayerMetric):
    """
    Base class for evaluating assists per game.
    Applies a standard NBA scale.
    """

    def evaluate(self):
        """General NBA assist rating."""
        if self.value >= 10:
            return ("Excellent", 5)
        elif self.value >= 7:
            return ("Good", 4)
        elif self.value >= 5:
            return ("OK", 3)
        elif self.value >= 3:
            return ("Bad", 2)
        else:
            return ("Terrible", 1)


class PointGuardAssists(AssistsMetric):
    """
    Specialized metric: PGs are expected to have higher APG.
    Overrides evaluate() for stricter grading.
    """

    def evaluate(self):
        if self.value >= 11:
            return ("Excellent", 5)
        elif self.value >= 8:
            return ("Good", 4)
        elif self.value >= 6:
            return ("OK", 3)
        elif self.value >= 4:
            return ("Bad", 2)
        else:
            return ("Terrible", 1)


class CenterAssists(AssistsMetric):
    """
    Specialized metric: Centers are not expected to assist as much.
    Overrides evaluate() for a more lenient scale.
    """

    def evaluate(self):
        if self.value >= 6:
            return ("Excellent", 5)
        elif self.value >= 4:
            return ("Good", 4)
        elif self.value >= 2:
            return ("OK", 3)
        elif self.value >= 1:
            return ("Bad", 2)
        else:
            return ("Terrible", 1)


# src/evaluator.py
class Evaluator:
    """
    Composition class that evaluates multiple NBA metrics.
    Holds PlayerMetric objects and runs their evaluations.
    """

    def __init__(self):
        self._metrics = []  # stores PlayerMetric instances

    def add_metric(self, metric):
        """
        Add a metric object into the evaluator.
        """
        self._metrics.append(metric)

    def run_all(self):
        """
        Runs evaluations for all stored metrics.
        Returns list of (player, type, text_rating, numeric_rating)
        """
        results = []
        for metric in self._metrics:
            text_rating, numeric_rating = metric.evaluate()
            results.append({
                "player": metric.player_name,
                "metric": type(metric).__name__,
                "rating": text_rating,
                "score": numeric_rating
            })
        return results


# main.py
from assists_metric import AssistsMetric, PointGuardAssists, CenterAssists
from evaluator import Evaluator

def main():
    evaluator = Evaluator()

    # User inputs (could come from Project 1 functions)
    evaluator.add_metric(PointGuardAssists("Chris Paul", 8.3))
    evaluator.add_metric(CenterAssists("Nikola Jokic", 9.2))
    evaluator.add_metric(AssistsMetric("Klay Thompson", 2.1))

    results = evaluator.run_all()

    for r in results:
        print(f"{r['player']} - {r['metric']}: {r['rating']} ({r['score']})")

if __name__ == "__main__":
    main()

# src/rebounds_metric.py

from player_metric import PlayerMetric

class ReboundsMetric(PlayerMetric):
    """
    Base class for evaluating rebounds per game.
    Applies a general NBA scale for all positions.
    """

    def evaluate(self):
        # Standard rebound expectations
        if self.value >= 12:
            return ("Excellent", 5)
        elif self.value >= 8:
            return ("Good", 4)
        elif self.value >= 5:
            return ("OK", 3)
        elif self.value >= 3:
            return ("Bad", 2)
        else:
            return ("Terrible", 1)


class BigManRebounds(ReboundsMetric):
    """
    Centers and power forwards are expected to rebound more,
    so the scale is stricter.
    """

    def evaluate(self):
        if self.value >= 14:
            return ("Excellent", 5)
        elif self.value >= 10:
            return ("Good", 4)
        elif self.value >= 7:
            return ("OK", 3)
        elif self.value >= 4:
            return ("Bad", 2)
        else:
            return ("Terrible", 1)


class GuardRebounds(ReboundsMetric):
    """
    Guards rebound less on average,
    so this scale is more forgiving.
    """

    def evaluate(self):
        if self.value >= 7:
            return ("Excellent", 5)
        elif self.value >= 5:
            return ("Good", 4)
        elif self.value >= 3:
            return ("OK", 3)
        elif self.value >= 2:
            return ("Bad", 2)
        else:
            return ("Terrible", 1)
