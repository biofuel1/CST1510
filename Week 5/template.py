def load_records(path):
    records = []
    
    with open(path) as file:
        for line in file:
            label, value, limit = line.strip().split(',')
            records.append(Record(label, float(value), float(limit)))

    return records

class Record:
    over_limit_count = 0
    total_records = 0
    
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

        Record.total_records += 1

        if self.is_over():
            Record.over_limit_count += 1

    def percent(self):
        return (self.value / self.limit) * 100

    def status(self):
        """Returns the status, three possible categories: OVER LIMIT (100%+), WARNING (90%+), OK"""

        percent = self.percent()
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

    def is_over(self):
        return True if self.percent() >= 100.0 else False

records = load_records('records_sample.txt')

for record in records:
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f" Label:  {record.label:>10}")
    print(f" Value:  {record.value:>10}")
    print(f" Limit:  {record.limit:>10}")
    print(f" Status: {record.status():>10}")
    print("=" * 34)
    print()

print(f"{Record.over_limit_count} of {Record.total_records} records are OVER LIMIT")