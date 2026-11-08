import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("records_sample.csv")
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else ("WARNING" if x >= 90 else "OK")
)

print(df)
print(df[df["status"] != "OK"])

status_counts = df.groupby("status").size()
print(status_counts)
df.to_csv("records_report.csv", index=False)

status_counts.plot(kind="bar")
plt.savefig("records_status.png")
