import csv
from datetime import datetime
import os
import streamlit as st

st.markdown("### Sleep")
sleep = st.slider("Sleep", 1, 10, 5, label_visibility="collapsed")
st.divider()

st.markdown("### Energy")
energy = st.slider("Energy", 1, 10, 5, label_visibility="collapsed")
st.divider()

st.markdown("### Mood")
mood = st.slider("Mood", 1, 10, 5, label_visibility="collapsed")
st.divider()

st.subheader("Brain Dump")
brain_dump = st.text_area(
    "Brain Dump",
    placeholder="Write down any thoughts, worries, or intentions...",
    height=100,
    label_visibility="collapsed",
)
if st.button("Submit"):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    file_path = "tracker.csv"
    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Sleep", "Energy", "Mood","Braindump"])
        writer.writerow([timestamp, sleep, energy, mood,brain_dump])