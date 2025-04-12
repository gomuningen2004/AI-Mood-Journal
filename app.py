import streamlit as st
from mood_analysis import analyze_mood
from database import init_db, insert_entry, fetch_entries
from visualization import plot_mood_trends

# Page configuration
st.set_page_config(page_title="AI Mood Journal", layout="centered")
st.title("🧠 AI-Powered Mood Journal")

# Initialize the database
init_db()

# Text input for journal entry
entry = st.text_area("Write about your day:", height=200)

# Analyze button
if st.button("Analyze Mood"):
    if entry.strip():
        mood = analyze_mood(entry)
        if mood.startswith("Error:"):
            st.error(f"Mood Detection Failed: {mood}")
        else:
            st.success(f"Mood Detected: **{mood}**")
            insert_entry(entry, mood)
    else:
        st.warning("Please write something before submitting.")

# Show mood trends
st.subheader("📈 Mood Trend Over Time")
data = fetch_entries()
plot_mood_trends(data)
