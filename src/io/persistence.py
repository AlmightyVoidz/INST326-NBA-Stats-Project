# io/persistence.py
import json
from pathlib import Path

DATA_FILE = Path("data/nba_data.json")

def save_data(data):
    """Save player stats to a JSON file"""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {DATA_FILE}")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data():
    """Load player stats from a JSON file"""
    if not DATA_FILE.exists():
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}
