class Source:
    """
    Represents an NBA data source (game, team, or player stats).
    """

    def __init__(self, source_id, name, source_type, data):
        if not source_id.strip():
            raise ValueError("Source ID cannot be empty.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if source_type.lower() not in {"game", "team", "player"}:
            raise ValueError("Type must be 'game', 'team', or 'player'.")
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary.")

        self._source_id = source_id
        self._name = name
        self._source_type = source_type
        self._data = data

    @property
    def name(self):
        return self._name

    @property
    def source_type(self):
        return self._source_type

    @property
    def data(self):
        return self._data

    def get_stat(self, stat_name):
        return self._data.get(stat_name, None)

    def __str__(self):
        return f"Source '{self._name}' ({self._source_type}, {len(self._data)} stats)"

    def __repr__(self):
        return f"Source('{self._source_id}', '{self._name}', '{self._source_type}')"
