
import streamlit as st
import random
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrkkHTjij_DyfzUxbF0Lw3LfsyzUnh9MU8MQ&s");
            background-size: cover;
            background-position: center;
        }}
               

        .stButton>button {{
            color: #000000;  /* ⚫ Black Text */
            font-size: 18px;
        }}
                </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()  # Call function to apply background


# Session state to store game progress
if "coins" not in st.session_state:
    st.session_state.coins = 50  # Starting coins
if "level" not in st.session_state:
    st.session_state.level = 1  # Starting level

# Word lists for different levels
words_easy = [
    {"word": "TEA", "hint": "A popular hot beverage"},
    {"word": "SUN", "hint": "A big ball of fire in the sky"},
    {"word": "DOG", "hint": "A loyal pet"},
]
words_medium = [
    {"word": "LION", "hint": "King of the jungle"},
    {"word": "PLANE", "hint": "Flies in the sky"},
    {"word": "FISH", "hint": "Lives in water"},
]
words_hard = [
    {"word": "ASTRONAUT", "hint": "Travels in space"},
    {"word": "ELEPHANT", "hint": "Largest land animal"},
    {"word": "PYRAMID", "hint": "Ancient Egyptian structure"},
]

# Select words based on level
if st.session_state.level == 1:
    word_list = words_easy
elif st.session_state.level == 2:
    word_list = words_medium
else:
    word_list = words_hard

# Select a random word
word_data = random.choice(word_list)
word = word_data["word"]

# Generate options (1 correct + random wrong words)
wrong_words = [w["word"] for w in word_list if w["word"] != word]
options = random.sample(wrong_words, min(len(wrong_words), 3)) + [word]
random.shuffle(options)

# UI Design
st.title("🧩 Word Puzzle Game with Levels")
st.subheader(f"💰 Coins: {st.session_state.coins} | 🎯 Level: {st.session_state.level}")
st.write(f"Hint: {word_data['hint']}")

# Word selection (Multiple Choice)
selected_word = st.radio("Choose the correct word:", options)

# Check Answer
if st.button("Submit"):
    if selected_word == word:
        st.session_state.coins += 10  # Correct answer: +10 coins
        st.success("🎉 Correct! You earned +10 coins!")
        
        # Level up if coins are enough
        if st.session_state.coins >= 50 and st.session_state.level == 1:
            st.session_state.level = 2
            st.session_state.coins -= 20  # Leveling up costs 20 coins
            st.info("🎯 Level Up! Welcome to Level 2!")
        elif st.session_state.coins >= 80 and st.session_state.level == 2:
            st.session_state.level = 3
            st.session_state.coins -= 30  # Leveling up costs 30 coins
            st.info("🚀 Level Up! Welcome to Level 3!")
        
    else:
        st.session_state.coins -= 5  # Wrong answer: -5 coins
        st.error("❌ Wrong! You lost -5 coins!")

# Reset Game
if st.button("🔄 Reset Game"):
    st.session_state.coins = 50
    st.session_state.level = 1
    st.info("🎮 Game has been reset!")
