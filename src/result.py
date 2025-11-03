from datetime import datetime

class Result:
    """
    Represents a single search result returned by a Query.

    Attributes:
        _source (Source): The source this result came from.
        _query (Query): The query that produced this result.
        _title (str): Title of the result.
        _snippet (str): Text snippet or summary from the document.
        _score (float): Relevance score between 0 and 1.
        _url (str): Link or identifier of the result.
        _retrieved_at (datetime): Timestamp when the result was created.
    """

    def __init__(self, source, query, title, snippet, score, url):
        # Basic validation
        if not title.strip():
            raise ValueError("Result title cannot be empty.")
        if not isinstance(score, (float, int)) or not (0 <= score <= 1):
            raise ValueError("Score must be a number between 0 and 1.")
        if not url.strip():
            raise ValueError("URL cannot be empty.")

        self._source = source
        self._query = query
        self._title = title
        self._snippet = snippet
        self._score = float(score)
        self._url = url
        self._retrieved_at = datetime.now()

    # ------------------------------
    # Properties (Encapsulation)
    # ------------------------------
    @property
    def title(self):
        """Get the result title (read-only)."""
        return self._title

    @property
    def score(self):
        """Get or set the result’s relevance score."""
        return self._score

    @score.setter
    def score(self, value):
        if not (0 <= value <= 1):
            raise ValueError("Score must be between 0 and 1.")
        self._score = float(value)

    @property
    def url(self):
        """Return the URL of the result."""
        return self._url

    @property
    def snippet(self):
        """Return a preview snippet of the result."""
        return self._snippet

    @property
    def retrieved_at(self):
        """Return timestamp when the result was created."""
        return self._retrieved_at

    # ------------------------------
    # Instance Methods
    # ------------------------------
    def summarize(self, max_chars=100):
        """
        Return a truncated summary of the snippet for display.
        """
        return self._snippet[:max_chars] + ("..." if len(self._snippet) > max_chars else "")

    def boost_score(self, factor):
        """
        Boost relevance score by a factor (for user feedback or click data).
        """
        new_score = min(self._score * factor, 1.0)
        self._score = new_score
        return new_score

    def to_dict(self):
        """
        Convert the result to a dictionary format (for saving or exporting).
        """
        return {
            "title": self._title,
            "snippet": self._snippet,
            "score": self._score,
            "url": self._url,
            "retrieved_at": self._retrieved_at.isoformat(),
            "source": getattr(self._source, "name", None),
            "query": getattr(self._query, "text", None)
        }

    def __str__(self):
        return f"{self._title} (score: {self._score:.2f})"

    def __repr__(self):
        return f"Result(title={self._title!r}, score={self._score:.2f}, url={self._url!r})"

