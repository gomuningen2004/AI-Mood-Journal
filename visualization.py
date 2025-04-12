import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def plot_mood_trends(data):
    if not data:
        st.info("No mood data to display yet.")
        return

    # Extract only timestamp and mood for plotting
    filtered_data = [(ts, mood) for ts, _, mood in data]
    df = pd.DataFrame(filtered_data, columns=["timestamp", "mood"])
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    valid_moods = [
        'Happy', 'Sad', 'Angry', 'Excited', 'Anxious', 'Calm',
        'Tired', 'Frustrated', 'Grateful', 'Joyful', 'Confused', 'Lonely'
    ]
    df = df[df['mood'].isin(valid_moods)]

    st.markdown("### 📈 Mood Trend Over Time")
    mood_counts = df.groupby([df['timestamp'].dt.date, 'mood']).size().unstack(fill_value=0)

    # Line Chart
    plt.figure(figsize=(10, 5))
    mood_counts.plot(ax=plt.gca(), marker='o')
    plt.title("Mood Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.legend(title="Mood", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(plt.gcf())

    # Bar Chart
    st.markdown("### 📊 Overall Mood Frequency")
    total_counts = df['mood'].value_counts().reindex(valid_moods, fill_value=0)

    fig, ax = plt.subplots(figsize=(8, 4))
    total_counts.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title("Total Mood Frequency")
    ax.set_xlabel("Mood")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)
