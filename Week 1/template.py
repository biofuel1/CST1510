label = input("Enter dataset name: ")    
first = float(input("Enter rows loaded: "))   
second = float(input("Enter rows expected: "))   

difference = first - second
percent = (first / second) * 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Rows loaded:    {first:>10.2f}")
print(f"  Rows expected:  {second:>10.2f}")
print(f"  Difference:     {difference:>+10.2f}")
print(f"  Percent loaded: {percent:>10.2f}%")
print(f"  Status:         {status}") # Printing the status is useful because it indicates whether the value exceeds the limit.

print("=" * 34)


