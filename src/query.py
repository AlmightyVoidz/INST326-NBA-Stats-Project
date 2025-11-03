from .source import Source

class Query:
    """
    Represents a query on NBA data sources (e.g., "Points > 100").
    """

    def __init__(self, query_id, search_stat, threshold=0):
        if not query_id.strip():
            raise ValueError("Query ID cannot be empty.")
        if not search_stat.strip():
            raise ValueError("Search stat cannot be empty.")
        if threshold < 0:
            raise ValueError("Threshold must be non-negative.")

        self._query_id = query_id
        self._search_stat = search_stat
        self._threshold = threshold
        self._results = []

    @property
    def search_stat(self):
        return self._search_stat

    @property
    def results(self):
        return self._results

    def execute(self, sources):
        if not all(isinstance(s, Source) for s in sources):
            raise TypeError("All items must be Source objects.")
        
        self._results = [
            {"source": s.name, self._search_stat: s.get_stat(self._search_stat)}
            for s in sources
            if s.get_stat(self._search_stat) is not None and s.get_stat(self._search_stat) >= self._threshold
        ]
        return self._results

    def __str__(self):
        return f"Query '{self._search_stat}' threshold={self._threshold}, {len(self._results)} results"

    def __repr__(self):
        return f"Query('{self._query_id}', '{self._search_stat}', threshold={self._threshold})"
