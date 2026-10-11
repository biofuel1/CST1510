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

def print_report(label, value, limit, difference, percent, status):
    """
    Prints the complete formatted report
    """

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used     :     {value}")
    print(f"  Total    :     {limit}")
    print(f"  Free     :     {-difference}")
    print(f"  Percent  :     {percent}")
    print(f"  Status   :     {status}")
    print("=" * 34)
    print()

overlimit_count = 0
while True:
    label = input("Enter label: ")
    if label == "quit":
        print(f"Your values went over limit {overlimit_count} times")
        break
    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        overlimit_count += 1
    print_report(label, value, limit, difference, percent, status)
