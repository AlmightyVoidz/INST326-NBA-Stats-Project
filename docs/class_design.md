### Rayyaan Dasti — NBA Statistical Analysis Classes

**Classes:** Source, Query

**Purpose:** 
- Source: Stores NBA game, team, or player stats.
- Query: Filters sources based on a specific stat and threshold.

**Encapsulation:** Private attributes (_attribute) with getters. Input validation ensures correct data types.

**Key Methods:**
- Source.get_stat(): Access a stat value.
- Query.execute(): Apply the query to multiple sources and store results.

**Example Usage:**
from src.source import Source
from src.query import Query

game1 = Source("G001", "Lakers vs Celtics", "game", {"points_lakers": 102})
query = Query("Q001", "points_lakers", 100)
results = query.execute([game1])
print(results)  # [{'source': 'Lakers vs Celtics', 'points_lakers': 102}]
