import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#defining file path

file_path = "tracker.csv"
df = pd.read_csv(file_path)

#cleaning up data
df.columns = df.columns.str.strip()
df["Timestamp"]= pd.to_datetime(df["Timestamp"])

numeric_col = ["Sleep","Energy","Mood"]
for col in numeric_col:
    df[col] = pd.to_numeric(df[col],errors="coerce")
# 