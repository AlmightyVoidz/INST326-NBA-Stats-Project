#1

import os

def extract_file_metadata(file_path):
    """Get basic info about a file.
    
    Args:
        file_path (str): The location of the file.
        
    Returns:
        dict: Includes name, type, and size in KB.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist.")
    
    file_name = os.path.basename(file_path)
    file_type = file_name.split(".")[-1]
    file_size = round(os.path.getsize(file_path) / 1024, 2)
    
    return {"name": file_name, "type": file_type, "size_kb": file_size}

#2

def tokenize_text(text):
    """Break text into lowercase words.
    
    Args:
        text (str): A string of text.
        
    Returns:
        list: List of lowercase words.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    text = text.lower()
    words = text.split()
    return words

#3

def count_word_frequency(words):
    """Count how many times each word appears.
    
    Args:
        words (list): List of words.
        
    Returns:
        dict: Word counts.
    """
    if not isinstance(words, list):
        raise TypeError("Input must be a list of words.")
    
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

#4

def find_keyword_in_text(text, keyword):
    """Check if a keyword appears in a text.
    
    Args:
        text (str): The text to search.
        keyword (str): The word to find.
        
    Returns:
        bool: True if found, False if not.
    """
    if not all(isinstance(x, str) for x in [text, keyword]):
        raise TypeError("Both text and keyword must be strings.")
    
    return keyword.lower() in text.lower()
#5

def make_snippet(text, keyword):
    """Make a short snippet showing where the keyword appears.
    
    Args:
        text (str): Full text.
        keyword (str): Word to highlight.
        
    Returns:
        str: Short snippet with keyword in the middle.
    """
    text_lower = text.lower()
    index = text_lower.find(keyword.lower())
    
    if index == -1:
        return text[:60] + "..." if len(text) > 60 else text
    
    start = max(0, index - 20)
    end = min(len(text), index + len(keyword) + 20)
    snippet = text[start:end]
    return f"...{snippet}..."

#6

import re

def clean_text(text: str) -> str:
    """This cleans strings by removing punctuation and making it lowercase."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned.lower().strip()

#7

def tokenize(text: str) -> list[str]:
    """ This Splits different texts into words."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    return clean_text(text).split()

#8

from collections import Counter

def word_frequency(text: str) -> dict[str, int]:
    """Counts how often each word appears."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    words = tokenize(text)
    return dict(Counter(words))

#9

def search_documents(query: str, documents: list[str]) -> list[int]:
    """Find which documents contain a given query term."""
    if not isinstance(query, str):
        raise TypeError("Query must be a string")
    if not isinstance(documents, list):
        raise TypeError("Documents must be a list of strings")
    
    query = query.lower()
    found = []
    for i, doc in enumerate(documents):
        if query in clean_text(doc):
            found.append(i)
    return found

#10

def highlight_term(text: str, term: str) -> str:
    """Highlights a word in text by surrounding it with brackets."""
    if not all(isinstance(i, str) for i in [text, term]):
        raise TypeError("Both inputs must be strings")
    pattern = re.compile(rf'\b{term}\b', re.IGNORECASE)
    return pattern.sub(f'[{term.upper()}]', text)
@@ -8,11 +8,29 @@ def word_count(text: str) -> int:

#11

def average_word_length(text: str) -> float:
    """Compute average word length in text."""
    if not text.strip():
        return 0
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    words = text.split()
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)

#12

def clean_text(text: str) -> str:
    """Trim spaces and lowercase text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return " ".join(text.strip().lower().split())

#13

def contains_keyword(text: str, keyword: str) -> bool:
    """Check if keyword appears in text (case-insensitive)."""
    if not isinstance(text, str) or not isinstance(keyword, str):
        raise TypeError("Both inputs must be strings")
    return keyword.lower() in text.lower()
#14


def summarize_text(text: str, limit: int = 10) -> str:
    """Return the first `limit` words of text."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer")
    return " ".join(text.split()[:limit])
