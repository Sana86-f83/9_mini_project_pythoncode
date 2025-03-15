import streamlit as st
import random

# Custom CSS for styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* General styling */
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #ffe4b5; /* Light orange background */
        color: #333;
        margin: 0;
        padding: 0;
    }

    /* White box styling */
    .content-box {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 800px;
        height: 400px;
        margin-top: 24px;
        position: absolute;
        left: 50%; 
        transform: translateX(-50%);
        border-radius: 14px;
        border: 1px solid #f9f9f9;
        backdrop-filter: blur(30px);
        box-shadow: 0px 4px 4px -1px rgba(0, 0, 0, 0.25);
    }

    h1, p, label{
    color: white !important;
    }

    /* Game title with gradient */
    .title {
        font-size: 3rem;
        font-weight: 600;
        text-align: center;
        margint-top:10px;
        background: linear-gradient(135deg, #ff8c42, #ff6f61); /* Orange gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
    }

    /* Footer styling */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #ff8c42, #ff6f61); /* Orange gradient */
        color: white;
        font-size: 1rem;
    }

    /* Input and button styling */
    .stTextInput, .stButton {
        text-align: center;
        margin: 0 auto;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state to store game variables
if 'word' not in st.session_state:
    st.session_state.word = ""
if 'turns' not in st.session_state:
    st.session_state.turns = 10
if 'guess_made' not in st.session_state:
    st.session_state.guess_made = ""
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Function to reset the game
def reset_game():
    st.session_state.word = random.choice(["python", "html", "php", "sql", "nextjs", "typescript"]).lower()
    st.session_state.turns = 10
    st.session_state.guess_made = ""
    st.session_state.game_over = False

# Function to display the hangman figure
def display_hangman(turns):
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    # Ensure the index is within the valid range
    index = min(10 - turns, len(hangman_stages) - 1)
    st.markdown(f'<pre>{hangman_stages[index]}</pre>', unsafe_allow_html=True)

# Main game logic
def hangman():
    # Game title with gradient
    st.markdown('<h1 class="title">Hangman Game</h1>', unsafe_allow_html=True)

    # Create a container for all content
    with st.container():
        st.markdown('<div class="content-box">', unsafe_allow_html=True)

        st.write("Guess the word in less than 10 attempts!")

        # Initialize the game if not already initialized
        if not st.session_state.word:
            reset_game()

        # Display the current state of the word
        main_word = ""
        for letter in st.session_state.word:
            if letter in st.session_state.guess_made:
                main_word += letter
            else:
                main_word += "_"
        st.write("Word:", main_word)

        # Check if the player has won
        if main_word == st.session_state.word:
            st.success("You won!!")
            st.session_state.game_over = True

        # Display the hangman figure
        display_hangman(st.session_state.turns)

        # Input for guessing a letter
        guess = st.text_input("Guess a letter:", max_chars=1, key="guess_input").lower()

        if st.button("Submit Guess"):
            if guess in "abcdefghijklmnopqrstuvwxyz":
                if guess not in st.session_state.guess_made:
                    st.session_state.guess_made += guess
                    if guess not in st.session_state.word:
                        st.session_state.turns -= 1
                        if st.session_state.turns == 0:
                            st.error("You lost! The word was: " + st.session_state.word)
                            st.session_state.game_over = True
                else:
                    st.warning("You already guessed that letter!")
            else:
                st.warning("Please enter a valid letter.")

        # Reset button to start a new game
        if st.session_state.game_over:
            if st.button("Play Again"):
                reset_game()

        st.markdown('</div>', unsafe_allow_html=True)

# Run the game
hangman()

# Footer with your name
st.markdown('<div class="footer">Created by Sana Faisal</div>', unsafe_allow_html=True)