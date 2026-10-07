import csv
from datetime import datetime
import os
import streamlit as st
import pandas as pd
from google import genai

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
    placeholder="Write down something for the day. (Check Side Bar For analysis)",
    height=100,
    label_visibility="collapsed",
)
if st.button("Submit"):
    now = datetime.now()
    timestamp = now.strftime("%m-%d %H:%M")
    file_path = "tracker.csv"
    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Sleep", "Energy", "Mood", "Brain dump"])
        writer.writerow([timestamp, sleep, energy, mood, brain_dump])
        st.balloons()

if os.path.exists("tracker.csv"):
    df = pd.read_csv("tracker.csv")
    recent = df.tail(7)
    
    st.sidebar.metric("Average Mood", f"{recent['Mood'].mean():.1f} / 10")
    st.sidebar.metric("Average Energy", f"{recent['Energy'].mean():.1f} / 10")
    st.sidebar.metric("Average Sleep", f"{recent['Sleep'].mean():.1f} / 10")


# Analysiny brain dump with ai 
with st.sidebar:
    st.divider()
    if st.button("Get reflection from AI"):
        with st.spinner("Reflecting..."):
            st.info(response.text)