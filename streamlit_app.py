import streamlit as st
import random

# Kleuren en hun namen
COLORS = {
    "Rood": "red",
    "Groen": "green",
    "Blauw": "blue",
    "Geel": "yellow",
    "Paars": "purple",
    "Oranje": "orange"
}

# App-instellingen
st.set_page_config(page_title="Strooptest", layout="centered")

# Variabelen initialiseren
if "score" not in st.session_state:
    st.session_state.score = 0
if "rounds" not in st.session_state:
    st.session_state.rounds = 0
if "current_color_name" not in st.session_state:
    st.session_state.current_color_name = None
if "current_color_code" not in st.session_state:
    st.session_state.current_color_code = None
max_rounds = 10

# Functie voor een nieuwe ronde
def new_round():
    if st.session_state.rounds < max_rounds:
        st.session_state.rounds += 1
        st.session_state.current_color_name = random.choice(list(COLORS.keys()))
        st.session_state.current_color_code = random.choice(list(COLORS.values()))

# Functie om antwoord te controleren
def check_answer(selected_color):
    if st.session_state.rounds <= max_rounds:
        if selected_color == st.session_state.current_color_code:
            st.session_state.score += 1
        new_round()

# Start nieuwe ronde als nodig
if st.session_state.rounds == 0:
    new_round()

# Interface
st.title("Strooptest")
st.write(
    "Kies de kleur waarin het woord is geschreven, niet wat het woord zegt!"
)
st.write(f"Ronde {min(st.session_state.rounds, max_rounds)} van {max_rounds}")

# Controleren of het spel voorbij is
if st.session_state.rounds > max_rounds:
    st.markdown(
        f"<h2 style='text-align: center;'>Einde van het spel!</h2>",
        unsafe_allow_html=True
    )
    st.write(f"Je score is: {st.session_state.score} van de {max_rounds}!")
    if st.button("Opnieuw spelen"):
        st.session_state.score = 0
        st.session_state.rounds = 0
        new_round()
else:
    # Kleurnaam weergeven
    st.markdown(
        f"<h1 style='text-align: center; color: {st.session_state.current_color_code};'>"
        f"{st.session_state.current_color_name}</h1>",
        unsafe_allow_html=True
    )

    # Kleurenknoppen
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    buttons = list(COLORS.items())
    random.shuffle(buttons)

    for i, (color_name, color_code) in enumerate(buttons):
        with cols[i % 3]:
            st.button(
                color_name,
                key=color_code,
                on_click=check_answer,
                args=(color_code,)
            )
