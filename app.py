import streamlit as st
from analyzer.strength_check import analyze_password_strength
from simulator.brute_force_estimator import estimate_brute_force_time
import bcrypt

st.set_page_config(page_title="Password Strength Analyzer", layout="centered")

st.title("Password Strength Analyzer")

# Inputfält
password = st.text_input("Skriv ett lösenord för analys", type="password")

if password:
    # Analysera styrka
    result = analyze_password_strength(password)

    st.subheader("Analysresultat")
    st.write(f"**Poäng:** {result['poäng']} / 6")
    st.write(f"**Klassificering:** {result['klassificering']}")

    # Färgindikator
    color = {
        "Svagt": "🔴",
        "Medel": "🟠",
        "Starkt": "🟢"
    }[result["klassificering"]]
    st.write(f"**Bedömning:** {color} {result['klassificering']}")

    # Förbättringstips
    if result["förbättringar"]:
        st.subheader("Förbättringsförslag")
        for tip in result["förbättringar"]:
            st.write("- " + tip)

    # Brute-force tid
    st.subheader("Estimerad brute-force tid")
    est_time = estimate_brute_force_time(password)
    st.write(f"*Ungefärlig tid att knäcka lösenordet:* **{est_time}**")

    # Visa hash
    st.subheader("Hashad version (bcrypt)")
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    st.code(hashed.decode(), language="bash")
