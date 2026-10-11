overlimit_count = 0
while True:
    label = input("Enter dataset name: ")

    if label == "quit":
        break

    value = float(input("Enter rows loaded: "))
    limit = float(input("Enter rows expected: "))

    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        overlimit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Rows loaded:    {value:>10.2f}")
    print(f"  Rows expected:  {limit:>10.2f}")
    print(f"  Difference:     {difference:>+10.2f}")
    print(f"  Percent:        {percent:>10.2f}%")
    print(f"  Status:         {status}")
    print("=" * 34)
    print()

print(f"Your values went over limit {overlimit_count} times")


