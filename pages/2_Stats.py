import streamlit as st
from database import fetch_entries
from visualization import plot_mood_trends

st.title("📊 Mood Statistics")

entries = fetch_entries()
plot_mood_trends(entries)
