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
