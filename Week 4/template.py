def status_of(percent):
    """
    Returns 'OVER LIMIT' if percentage is 100% or more, and 'WARNING' if it is 90% or more
    """

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """
    Calculates the difference and the percentage, and returns the two values in a tuple
    """

    difference = value - limit
    percent = (value / limit) * 100
    return difference, round(percent, 2)

def check_record(value, limit):
    """
    Return the difference, percentage and status for a record
    """

    difference, percent = check(value, limit)
    status = status_of(percent)
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """
    Prints the complete formatted report
    """

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Rows loaded   :     {value}")
    print(f"  Rows expected :     {limit}")
    print(f"  Rows missing  :     {-difference}")
    print(f"  Percent       :     {percent}")
    print(f"  Status        :     {status}")
    print("=" * 34)
    print()

def load_records(path):
    """
    Load records from a text file
    """

    records = []

    with open(path) as data_file:
        for line in data_file:
            label, value, limit = line.strip().split(",")
            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }
            records.append(record)

    return records

try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("Could not find records.txt! Starting with an empty list.")
    records = []

overlimit_count = 0

with open("results.txt", "w") as results_file:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])

        if status == "OVER LIMIT":
            overlimit_count += 1

        print_report(record["label"], record["value"], record["limit"], difference, percent, status)
        results_file.write(f'{record["label"]},{status}\n')

print(f"Number of records over limit: {overlimit_count}")
