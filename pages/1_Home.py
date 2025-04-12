import streamlit as st
from mood_analysis import analyze_mood
from database import init_db, insert_entry, fetch_entries

st.title("📓 Journal Home")

# Initialize the database
init_db()

# Input journal entry
entry = st.text_area("Write about your day:", height=200)

# Analyze mood and save
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

# View entries
st.subheader("📚 View Journal Entries")
entries = fetch_entries()

# Mood filter
all_moods = list(set([mood for _, _, mood in entries]))
selected_mood = st.selectbox("Filter by Mood", ["All"] + sorted(all_moods))

filtered_entries = [
    (ts, entry, mood) for ts, entry, mood in entries
    if selected_mood == "All" or mood == selected_mood
]

# Display filtered entries
for ts, entry, mood in filtered_entries:
    with st.expander(f"[{ts[:19]}] Mood: {mood}"):
        st.write(entry)
