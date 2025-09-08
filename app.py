import streamlit as st
import random

st.title("Tren på å gange og dele med 10, 100 og 1000")

# Velg operasjon
operation = st.selectbox("Velg regneoperasjon:", ["Gange", "Dele"])

# Velg faktor
factor = st.selectbox("Velg faktor:", [10, 100, 1000])

# Generer et tilfeldig tall
number = st.number_input("Tall å regne med:", min_value=1, max_value=10000, value=random.randint(1, 10000), step=1)

# Brukeren skal skrive inn svaret
user_answer = st.number_input("Skriv inn svaret:", value=0)

# Sjekk svaret
if st.button("Sjekk svar"):
    if operation == "Gange":
        correct_answer = number * factor
        op_str = f"{number} × {factor}"
    else:
        correct_answer = number / factor
        op_str = f"{number} ÷ {factor}"

    if user_answer == correct_answer:
        st.success(f"Riktig! {op_str} = {correct_answer}")
    else:
        st.error(f"Feil. {op_str} = {correct_answer}")

st.markdown("""
Tips: Du kan enkelt publisere denne appen på Streamlit Cloud.
""")