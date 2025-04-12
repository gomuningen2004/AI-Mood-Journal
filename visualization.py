import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def plot_mood_trends(data):
    if not data:
        st.info("No mood data to display yet.")
        return

    df = pd.DataFrame(data, columns=["timestamp", "entry", "mood"])
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Filter only valid moods for plotting
    valid_moods = ['Happy', 'Sad', 'Angry', 'Excited', 'Anxious', 'Calm', 'Tired', 'Frustrated', 'Grateful', 'Joyful', 'Confused', 'Lonely']
    df = df[df['mood'].isin(valid_moods)]

    mood_counts = df.groupby(['timestamp', 'mood']).size().unstack(fill_value=0)

    plt.figure(figsize=(10, 5))
    mood_counts.plot(ax=plt.gca(), marker='o')
    plt.title("Mood Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.legend(title="Mood")
    st.pyplot(plt.gcf())
