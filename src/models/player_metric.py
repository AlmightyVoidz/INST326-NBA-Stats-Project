# models/player_metric.py
from abc import ABC, abstractmethod

class AbstractStat(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def rate(self):
        pass

# Shooting, Scoring, Defense Stats
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

# Assists
class PlayerMetric(ABC):
    def __init__(self, player_name, value):
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
        pass

class AssistsMetric(PlayerMetric):
    def evaluate(self):
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

# Rebounds
class ReboundsMetric(PlayerMetric):
    def evaluate(self):
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



