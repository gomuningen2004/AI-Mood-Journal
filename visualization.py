import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def plot_mood_trends(data):
    if not data:
        st.info("No mood data to display yet.")
        return

    # Extract timestamp and mood
    filtered_data = [(ts, mood) for ts, _, mood in data]
    df = pd.DataFrame(filtered_data, columns=["timestamp", "mood"])
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    valid_moods = [
        'Happy', 'Sad', 'Angry', 'Excited', 'Anxious', 'Calm',
        'Tired', 'Frustrated', 'Grateful', 'Joyful', 'Confused', 'Lonely'
    ]
    df = df[df['mood'].isin(valid_moods)]

    # Date filtering UI
    st.markdown("### 📅 Filter by Date, Month, or Year")

    df['date'] = df['timestamp'].dt.date
    df['month'] = df['timestamp'].dt.strftime('%Y-%m')
    df['year'] = df['timestamp'].dt.year

    filter_type = st.radio("Choose a filter type:", ["Date", "Month", "Year", "All"], horizontal=True)

    if filter_type == "Date":
        selected_date = st.date_input("Select a date")
        df = df[df['date'] == selected_date]
    elif filter_type == "Month":
        months = sorted(df['month'].unique())
        selected_month = st.selectbox("Select a month", months)
        df = df[df['month'] == selected_month]
    elif filter_type == "Year":
        years = sorted(df['year'].unique())
        selected_year = st.selectbox("Select a year", years)
        df = df[df['year'] == selected_year]

    # Doughnut chart for mood distribution
    st.markdown("### 🍩 Mood Distribution")

    mood_distribution = df['mood'].value_counts()
    mood_distribution = mood_distribution[mood_distribution > 0]  # remove 0s

    if mood_distribution.empty:
        st.warning("No mood data available for this filter.")
        return

    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        mood_distribution,
        labels=mood_distribution.index,
        autopct='%1.1f%%',
        startangle=140,
        pctdistance=0.85,
        colors=plt.cm.tab20.colors
    )

    # Draw a circle at the center to turn it into a doughnut
    centre_circle = plt.Circle((0, 0), 0.60, fc='white')
    fig.gca().add_artist(centre_circle)

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.setp(autotexts, size=10, weight="bold", color="black")
    plt.setp(texts, size=10)

    # ax.set_title("Mood Distribution", fontsize=14)
    st.pyplot(fig)
