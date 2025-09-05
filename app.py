import streamlit as st

# Title
st.title("🌟 AI Mood-Based Daily Quotes")

# Ask user for mood input
mood = st.text_input("How are you feeling today? (happy, sad, stressed)")

# Simple mood-based responses
quotes = {
    "happy": "😊 Keep shining! Your happiness is contagious.",
    "sad": "🌈 Tough times never last, but tough people do.",
    "stressed": "🧘 Take a deep breath, you are stronger than you think."
}

if mood:
    mood = mood.lower()
    if mood in quotes:
        st.success(quotes[mood])
    else:
        st.warning("Sorry, I don't have a quote for that mood yet.")
