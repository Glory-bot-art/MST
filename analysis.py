import pandas as pd
import matplotlib.pyplot as plt

#defining file path

file_path = "tracker.csv"
df = pd.read_csv(file_path)

#cleaning up data
df.columns = df.columns.str.strip()
df["Timestamp"]= pd.to_datetime(df["Timestamp"])
df["Date"] = df["Timestamp"].dt.date


daily_summary = df.groupby("Date")[["Sleep","Energy","Mood"]].mean()
print("Daily Averages")
print(daily_summary)