
import random
import streamlit as st

quotes = {
    "happy": [
        "Keep shining, the world needs your light! 🌟",
        "Happiness looks good on you. Keep smiling! 😊",
        "Spread your joy, it's contagious!",
        "Your energy is inspiring—share it with others!",
        "Celebrate the little moments, they add up to happiness!"
    ],
    "sad": [
        "It's okay to feel sad, brighter days are coming 🌈",
        "Tough times never last, but tough people do 💪",
        "Your story isn't over yet—keep going ❤️",
        "Even the darkest night will end and the sun will rise 🌞",
        "You are loved, even if it doesn’t feel like it right now."
    ],
    "stressed": [
        "Take a deep breath, relax. You're doing better than you think 🌿",
        "Focus on one step at a time, not the whole staircase 🪜",
        "Rest is also productive. Don’t forget to care for yourself 🕊️",
        "Drink some water and stretch—your mind will thank you 💧",
        "Slow down. Nothing is under control anyway, and that’s okay!"
    ],
    "angry": [
        "Pause. Breathe. Respond, don’t react 😌",
        "Anger is like holding hot coal—let it go before it burns you 🔥",
        "Peace begins with you. Choose calm over chaos 🌸",
        "Don’t let anger control you, let kindness win 🕊️",
        "Count to ten before reacting—it works!"
    ],
    "lonely": [
        "You may feel alone, but remember—you are connected to everyone 🌍",
        "Reach out to a friend today, even a small message matters 📱",
        "You are never truly alone; your presence matters 💙",
        "Sometimes solitude brings strength—use it to recharge 🔋",
        "There’s always someone who cares about you. Don’t forget that ❤️"
    ],
    "excited": [
        "Your excitement is your superpower—use it wisely ⚡",
        "Chase your dreams with that energy! 🚀",
        "Excitement is the spark of creativity—follow it 🎨",
        "Celebrate your wins, no matter how small 🎉",
        "Your enthusiasm will inspire others around you 🌟"
    ],
    "tired": [
        "Rest is not a waste of time—it’s fuel for success 💤",
        "Sleep well, tomorrow needs your energy 🌙",
        "Your body speaks through tiredness—listen and care for it ❤️",
        "Take a break. Even machines need to recharge 🔋",
        "Don’t push too hard, slow progress is still progress 🐢"
    ],
    "default": [
        "Stay positive and believe in yourself! ✨",
        "Every day is a new chance to grow 🌱",
        "You are stronger than you think 💪",
        "Be kind to yourself—you are doing your best ❤️",
        "Life is a journey, not a race. Walk at your own pace 🚶"
    ]
}

def get_quote(mood):
    mood = mood.lower()
    if mood in quotes:
        return random.choice(quotes[mood])
    else:
        return random.choice(quotes["default"])

st.set_page_config(page_title="AI Mood-Based Daily Quotes", page_icon="🌟", layout="centered")

st.title("🌟 AI Mood-Based Daily Quotes 🌟")
st.write("Get personalized motivational quotes, calming tips, or advice based on your mood.")

mood = st.selectbox(
    "How are you feeling today?",
    ["happy", "sad", "stressed", "angry", "lonely", "excited", "tired", "other"]
)

if st.button("Get My Quote"):
    if mood == "other":
        st.success(get_quote("default"))
    else:
        st.success(get_quote(mood))
