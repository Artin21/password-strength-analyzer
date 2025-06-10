import math

# Antal gissningar per sekund – realistiskt för moderna GPU:er
GUESSES_PER_SECOND = 1_000_000_000  # 1 miljard

def estimate_brute_force_time(password: str) -> str:
    charset_size = 0

    # Beräkna hur många typer av tecken som används
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32  # ungefärligt antal specialtecken

    # Totalt antal möjliga kombinationer
    total_combinations = charset_size ** len(password)

    # Tid i sekunder
    seconds = total_combinations / GUESSES_PER_SECOND

    return format_time(seconds)


def format_time(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.2f} sekunder"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.2f} minuter"
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.2f} timmar"
    days = hours / 24
    if days < 365:
        return f"{days:.2f} dagar"
    years = days / 365
    return f"{years:.2f} år"
