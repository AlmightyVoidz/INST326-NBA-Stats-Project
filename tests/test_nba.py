from src.source import Source
from src.query import Query

# Create example NBA game sources
game1 = Source("G001", "Lakers vs Celtics", "game", {"points_lakers": 102, "points_celtics": 99})
game2 = Source("G002", "Bulls vs Heat", "game", {"points_bulls": 110, "points_heat": 105})

# Create a query to find games where Lakers scored at least 100 points
query = Query("Q001", "points_lakers", 100)
results = query.execute([game1, game2])
print(results)
