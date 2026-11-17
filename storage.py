import csv
from pathlib import Path

FIELDS = ["test_id","date_time","project","location","batch","truck","mix",
          "technician","slump_in","minimum_in","maximum_in","status","notes"]

class CSVStorage:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            with self.path.open("w", newline="", encoding="utf-8") as f:
                csv.DictWriter(f, fieldnames=FIELDS).writeheader()

    def save(self, record):
        with self.path.open("a", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writerow(record)

    def load(self):
        with self.path.open("r", newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
