from datetime import datetime
from uuid import uuid4
from storage import CSVStorage

class SlumpTestManager:
    def __init__(self, path="data/slump_tests.csv"):
        self.store = CSVStorage(path)

    def add(self, **v):
        if v["minimum"] > v["maximum"]:
            raise ValueError("Minimum slump cannot exceed maximum.")
        value = v["slump"]
        record = {
            "test_id": str(uuid4())[:8].upper(),
            "date_time": datetime.now().astimezone().isoformat(timespec="seconds"),
            "project": v["project"], "location": v["location"],
            "batch": v["batch"], "truck": v["truck"], "mix": v["mix"],
            "technician": v["technician"], "slump_in": f'{value:.2f}',
            "minimum_in": f'{v["minimum"]:.2f}', "maximum_in": f'{v["maximum"]:.2f}',
            "status": "PASS" if v["minimum"] <= value <= v["maximum"] else "OUT OF RANGE",
            "notes": v["notes"]
        }
        self.store.save(record)
        return record

    def history(self):
        return self.store.load()
