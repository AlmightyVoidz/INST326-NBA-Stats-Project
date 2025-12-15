# io/importer.py
import csv
from pathlib import Path

def import_csv(file_path):
    """Import player stats from a CSV file"""
    path = Path(file_path)
    if not path.exists():
        print(f"File {file_path} not found.")
        return []

    players = []
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            players.append(row)
    return players
