import streamlit as st
from mood_analysis import analyze_mood
from database import init_db, insert_entry, fetch_entries

st.set_page_config(page_title="Journal Home", layout="centered")
st.title("📓 Journal Home")

# Initialize DB
init_db()

# Mood-color mapping
mood_colors = {
    "Happy": "#28a745",     # green
    "Sad": "#007bff",       # blue
    "Angry": "#dc3545",     # red
    "Calm": "#17a2b8",      # teal
    "Anxious": "#ffc107",   # yellow
    "Excited": "#6610f2",   # purple
    "Neutral": "#6c757d",   # gray
}

# Entry input
entry = st.text_area("Write about your day:", height=200)

# Mood Analysis
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

# Show entries
st.subheader("📚 View Journal Entries")
entries = fetch_entries()

# Mood filter
all_moods = list(set([mood for _, _, mood in entries]))
selected_mood = st.selectbox("Filter by Mood", ["All"] + sorted(all_moods))

filtered_entries = [
    (ts, entry, mood) for ts, entry, mood in entries
    if selected_mood == "All" or mood == selected_mood
]

# Show entries as colored cards
for ts, entry_text, mood in reversed(filtered_entries):
    color = mood_colors.get(mood, "#6c757d")  # fallback gray

    card_html = f"""
    <div class="card" style="
        margin-bottom: 1rem;
        border: 2px solid {color};
        border-radius: 0.75rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
      <div class="card-body" style="padding: 1rem;">
        <span style="
            background-color: {color};
            color: white;
            padding: 4px 10px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;">
          {mood}
        </span>
        <p style="margin-top: 0.75rem; font-size: 1rem; line-height: 1.5;">
          {entry_text}
        </p>
      </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
