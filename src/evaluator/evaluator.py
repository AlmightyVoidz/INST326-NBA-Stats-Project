# evaluator/evaluator.py
class Evaluator:
    def __init__(self):
        self._metrics = []

    def add_metric(self, metric):
        self._metrics.append(metric)

    def run_all(self):
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
