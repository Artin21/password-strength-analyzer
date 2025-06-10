import re

def analyze_password_strength(password: str) -> dict:
    score = 0
    suggestions = []

    # Kolla längd
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Använd minst 12 tecken.")

    # Stora bokstäver
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Lägg till stora bokstäver.")

    # Små bokstäver
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Lägg till små bokstäver.")

    # Siffror
    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Lägg till siffror.")

    # Specialtecken
    if re.search(r'[\W_]', password):
        score += 1
    else:
        suggestions.append("Lägg till specialtecken (!@# osv).")

    # Klassificering
    if score <= 2:
        strength = "Svagt"
    elif score <= 4:
        strength = "Medel"
    else:
        strength = "Starkt"

    return {
        "poäng": score,
        "klassificering": strength,
        "förbättringar": suggestions
    }
