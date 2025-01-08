import streamlit as st
import random

# Kleuren en namen
COLORS = {
    "Rood": "red",
    "Groen": "green",
    "Blauw": "blue",
    "Geel": "yellow",
    "Paars": "purple",
    "Oranje": "orange"
}

# Functie voor nieuwe ronde
def new_round():
    color_name = random.choice(list(COLORS.keys()))
    color_code = random.choice(list(COLORS.values()))
    return color_name, color_code

# Streamlit GUI
st.title("Strooptest")
st.write("Kies de kleur waarin het woord geschreven is, niet wat het woord zegt!")

# Initialiseer sessiestatus
if "rounds" not in st.session_state:
    st.session_state.rounds = 0
    st.session_state.score = 0
    st.session_state.color_name, st.session_state.color_code = new_round()

# Check of het spel klaar is
if st.session_state.rounds < 10:
    # Toon kleur en tekst
    st.markdown(
        f"<h1 style='color:{st.session_state.color_code};'>{st.session_state.color_name}</h1>",
        unsafe_allow_html=True,
    )

    # Maak knoppen voor elke kleur
    for name, code in COLORS.items():
        if st.button(name):
            # Controleer of de gekozen kleur correct is
            if code == st.session_state.color_code:
                st.session_state.score += 1
            
            # Nieuwe ronde starten
            st.session_state.rounds += 1
            st.session_state.color_name, st.session_state.color_code = new_round()
            
            # Clear the Streamlit cache for reactive updates
            st.experimental_rerun()
else:
    # Toon de eindscore
    st.write(f"Je score is: {st.session_state.score} van de 10!")
