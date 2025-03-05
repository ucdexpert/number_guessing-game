import streamlit as st
import random

# Function to initialize/reset the game
def initialize_game():
    st.session_state.number = random.randint(st.session_state.min_range, st.session_state.max_range)
    st.session_state.attempts = 0
    st.session_state.hints_used = 0

# Initialize session state variables
if "number" not in st.session_state:
    st.session_state.min_range = 1
    st.session_state.max_range = 100
    st.session_state.difficulty = "Easy 😊"
    initialize_game()

# Streamlit App Title
st.title("🔥 Muhammad Uzair's Ultimate Number Guessing Game! 🎮🔢")

# Sidebar for settings
with st.sidebar:
    st.header("⚙ Settings")
    min_range = st.number_input("Minimum Range", value=st.session_state.min_range, min_value=1)
    max_range = st.number_input("Maximum Range", value=st.session_state.max_range, min_value=min_range + 1)

    if min_range != st.session_state.min_range or max_range != st.session_state.max_range:
        st.session_state.min_range = min_range
        st.session_state.max_range = max_range
        initialize_game()

    st.session_state.difficulty = st.selectbox("Difficulty Level", ["Easy 😊", "Medium 🤔", "Hard 🧠"])
    if st.button("🔄 Reset Game"):
        initialize_game()

# Set attempts limit based on difficulty
if st.session_state.difficulty == "Easy 😊":
    max_attempts = 10
elif st.session_state.difficulty == "Medium 🤔":
    max_attempts = 7
else:
    max_attempts = 5

# Display instructions
st.write(f"🔢 Guess a number between **{st.session_state.min_range}** and **{st.session_state.max_range}**")
st.write(f"🕹 Difficulty: **{st.session_state.difficulty}**")

# Hints System
if st.button("💡 Get a Hint"):
    if st.session_state.hints_used < 3:
        st.session_state.hints_used += 1
        number = st.session_state.number
        hint = random.choice([
            f"📌 The number is {'Even' if number % 2 == 0 else 'Odd'}",
            f"📌 The number is {'Greater' if number > (st.session_state.max_range // 2) else 'Smaller'} than {st.session_state.max_range // 2}",
            f"📌 The number is a multiple of {random.choice([2, 5, 10])}." if number % 2 == 0 or number % 5 == 0 else "📌 No special multiples."
        ])
        st.info(hint)
    else:
        st.warning("🚫 No more hints available!")

# User input for guessing
guess = st.number_input("🔢 Enter your guess", min_value=st.session_state.min_range, max_value=st.session_state.max_range)

if st.button("🚀 Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.error("📉 Too low!")
    elif guess > st.session_state.number:
        st.error("📈 Too high!")
    else:
        st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
        st.balloons()
        initialize_game()

    # Check if attempts are exhausted
    if st.session_state.attempts >= max_attempts and guess != st.session_state.number:
        st.error(f"😢 Game over! The correct number was **{st.session_state.number}**.")
        initialize_game()

# Display number of attempts
st.write(f"📊 Attempts: {st.session_state.attempts}/{max_attempts}")
