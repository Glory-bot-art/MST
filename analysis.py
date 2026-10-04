import pandas as pd

#defining file path

file_path = "tracker.csv"
df = pd.read_csv(file_path)

#cleaning up data
df.columns = df.columns.str.strip()
df["Timestamp"]= pd.to_datetime(df["Timestamp"])
df["Date"] = df["Timestamp"].dt.date

#calculating mean in to one 
df['Rating'] = df[['Sleep','Mood','Energy']].mean(axis=1)

#defining brain dump 
journal = df.dropna(subset=['Brain Dump'])

for index, row in journal.iterrows():
    clean_notes = str(row['Brain Dump']).strip()
    print(f"{row['Date']} | Rating: {row['Rating']:.1f}/10 | {clean_notes}")