import streamlit as st

st.set_page_config(page_title="AI Mood Journal", layout="centered")

st.title("🧠 Welcome to the AI Mood Journal")

st.markdown("""
Track your feelings, understand your emotional patterns, and gain insights using AI-powered sentiment analysis.
""")

# Add navigation-style buttons
st.markdown("### 🌐 Navigate to:")
col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Go to Home"):
        st.switch_page("pages/1_Home.py")

with col2:
    if st.button("📊 Go to Stats"):
        st.switch_page("pages/2_Stats.py")

# Add image or illustration
st.image("https://media.giphy.com/media/3orieRzvBJA0uSgvTG/giphy.gif", use_column_width=True)
