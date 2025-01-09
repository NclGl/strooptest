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

MAX_ROUNDS = 20

# App-instellingen
st.set_page_config(page_title="Strooptest", layout="centered")

# Initialiseer sessiestatus
if "score" not in st.session_state:
    st.session_state.score = 0
if "rounds" not in st.session_state:
    st.session_state.rounds = 0
if "current_color_name" not in st.session_state:
    st.session_state.current_color_name = None
if "current_color_code" not in st.session_state:
    st.session_state.current_color_code = None

def new_round():
    """Start een nieuwe ronde."""
    st.session_state.current_color_name = random.choice(list(COLORS.keys()))
    st.session_state.current_color_code = random.choice(list(COLORS.values()))

def check_answer(selected_color):
    """Controleer het antwoord van de gebruiker."""
    if selected_color == st.session_state.current_color_code:
        st.session_state.score += 1

    # Alleen nieuwe ronde starten als we nog niet klaar zijn
    if st.session_state.rounds <= MAX_ROUNDS:
        st.session_state.rounds += 1
        if st.session_state.rounds <= MAX_ROUNDS:
            new_round()

# Start de eerste ronde
if st.session_state.rounds == 0:
    st.session_state.rounds += 1
    new_round()

# Interface
st.title("Strooptest")
st.write("Kies de kleur waarin het woord is geschreven, niet wat het woord zegt!")

if st.session_state.rounds <= MAX_ROUNDS:
    # Toon huidige ronde en kleur
    st.write(f"Ronde {st.session_state.rounds} van {MAX_ROUNDS}")
    st.markdown(
        f"<h1 style='text-align: center; color: {st.session_state.current_color_code};'>"
        f"{st.session_state.current_color_name}</h1>",
        unsafe_allow_html=True
    )

    # Kleurenknoppen
    col0, col1, col2, col3, col4 = st.columns(5)
    cols = [col1, col2, col3]
    buttons = list(COLORS.items())

    with col0:
        pass
    with col4:
        pass
    
    for i, (color_name, color_code) in enumerate(buttons):
        with cols[i % 3]:
            st.button(
                color_name,
                key=f"{color_code}_{st.session_state.rounds}",  # Unieke sleutel per ronde
                on_click=check_answer,
                args=(color_code,)
            )
    print(st.session_state.rounds)
else:
    # Spel is afgelopen
    st.markdown(
        f"<h2 style='text-align: center;'>Einde van het spel!</h2>",
        unsafe_allow_html=True
    )
    st.write(f"Je uiteindelijke score is: **{st.session_state.score}**/**{MAX_ROUNDS}**!")
    
    st.session_state.score = 0
    st.session_state.rounds = 0
    
    if st.button("Opnieuw spelen"):
        # Reset alle sessiestatusvariabelen
        new_round()
