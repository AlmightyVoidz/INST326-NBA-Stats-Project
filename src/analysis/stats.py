# analysis/stats.py
def average_stat(metrics, metric_type):
    """Compute average value for a given metric type"""
    values = [m.value for m in metrics if type(m).__name__ == metric_type]
    if not values:
        return 0
    return sum(values) / len(values)
