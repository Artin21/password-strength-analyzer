# Password Strength Analyzer

Ett verktyg för att analysera hur starkt ett lösenord är, uppskatta tiden det skulle ta att brute-force-knäcka det, samt ge förbättringsförslag.

## Funktioner

- Bedömer lösenordets styrka (poäng och klassificering)
- Ger konkreta tips för att förbättra lösenord
- Visar teoretisk brute-force tid
- Genererar en hashad version av lösenordet (bcrypt)
- Enkelt och interaktivt webbgränssnitt (Streamlit)

## Så här kör du

Kör följande i din terminal:

```bash
# 1. Klona projektet
git clone https://github.com/<ditt-användarnamn>/password-strength-analyzer.git
cd password-strength-analyzer

# 2. Installera beroenden
pip install -r requirements.txt

# 3. Starta appen
streamlit run app.py
