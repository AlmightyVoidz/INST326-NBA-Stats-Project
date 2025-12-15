# io/exporter.py
import csv
from pathlib import Path

def export_csv(file_path, data):
    """Export player ratings to a CSV file"""
    path = Path(file_path)
    if not data:
        print("No data to export.")
        return

    keys = data[0].keys()
    try:
        with open(path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"Data exported to {file_path}")
    except Exception as e:
        print(f"Error exporting data: {e}")
