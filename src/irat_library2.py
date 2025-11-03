#Team Project 2

class Index:
"""Represents a searchable index of documents for information retrieval.

```
Attributes:
    _documents (dict): A mapping of document IDs to text content.
    _inverted_index (dict): A mapping of terms to sets of document IDs.

Example:
    >>> idx = Index()
    >>> idx.add_document("doc1", "Python is a programming language")
    >>> idx.add_document("doc2", "Python can be used for information retrieval")
    >>> idx.search("python")
    {'doc1', 'doc2'}
"""

def __init__(self):
    """Initialize an empty index."""
    self._documents = {}
    self._inverted_index = {}

@property
def documents(self):
    """dict: Access the stored documents (read-only)."""
    return self._documents.copy()

def add_document(self, doc_id, text):
    """Add a document to the index.
    
    Args:
        doc_id (str): Unique document identifier.
        text (str): The text content of the document.
    
    Raises:
        ValueError: If doc_id already exists or text is empty.
    """
    if not isinstance(doc_id, str) or not doc_id.strip():
        raise ValueError("Document ID must be a non-empty string.")
    if doc_id in self._documents:
        raise ValueError(f"Document ID '{doc_id}' already exists.")
    if not text.strip():
        raise ValueError("Document text cannot be empty.")

    self._documents[doc_id] = text
    self._index_document(doc_id, text)

def _index_document(self, doc_id, text):
    """Private method: update the inverted index with new document terms."""
    terms = text.lower().split()
    for term in terms:
        if term not in self._inverted_index:
            self._inverted_index[term] = set()
        self._inverted_index[term].add(doc_id)

def search(self, term):
    """Search for a term in the index and return matching document IDs.
    
    Args:
        term (str): Term to search for.
    
    Returns:
        set: Set of document IDs containing the term.
    """
    term = term.lower()
    return self._inverted_index.get(term, set())

def __len__(self):
    """Return the number of documents in the index."""
    return len(self._documents)

def __str__(self):
    return f"Index with {len(self)} documents and {len(self._inverted_index)} unique terms."

def __repr__(self):
    return f"Index(num_docs={len(self)}, num_terms={len(self._inverted_index)})"
```

class Report:
"""Generates analytical reports based on an Index.

```
Attributes:
    _index (Index): The Index instance being analyzed.

Example:
    >>> idx = Index()
    >>> idx.add_document("doc1", "data science uses python")
    >>> idx.add_document("doc2", "python is used in AI")
    >>> report = Report(idx)
    >>> print(report.top_terms())
    [('python', 2), ('uses', 1), ('used', 1)]
"""

def __init__(self, index):
    """Initialize a Report for a given Index.
    
    Args:
        index (Index): The index to generate reports for.
    
    Raises:
        TypeError: If index is not an Index instance.
    """
    if not isinstance(index, Index):
        raise TypeError("Report must be initialized with an Index instance.")
    self._index = index

@property
def total_documents(self):
    """int: Return the number of documents in the index."""
    return len(self._index)

def top_terms(self, n=5):
    """Return the top n most frequent terms in the index.
    
    Args:
        n (int): Number of terms to return (default 5).
    
    Returns:
        list[tuple[str, int]]: List of (term, frequency) pairs.
    """
    term_freq = {term: len(docs) for term, docs in self._index._inverted_index.items()}
    sorted_terms = sorted(term_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_terms[:n]

def document_summary(self):
    """Return a summary of all documents and their word counts."""
    return {doc_id: len(text.split()) for doc_id, text in self._index.documents.items()}

def generate_text_report(self):
    """Return a formatted text summary report."""
    lines = [
        f"INFORMATION RETRIEVAL REPORT",
        f"Total Documents: {self.total_documents}",
        f"Top Terms: {self.top_terms()}",
    ]
    return "\n".join(lines)

def __str__(self):
    return f"Report for Index with {self.total_documents} documents."

def __repr__(self):
    return f"Report(index_docs={self.total_documents})"
```

