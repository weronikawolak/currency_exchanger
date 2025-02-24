from typing import Dict

# Walidacja danych wejściowych
def validate_input_currency(currency: str, currencies: Dict[str, float]) -> bool:
    if currency in currencies:
        return True
    else:
        print(f"Niepoprawny kod waluty: {currency}. Dostępne waluty: {', '.join(currencies.keys())}.")  # Dodany komunikat z dostępnych walut
        return False

def validate_input_amount(amount: str) -> float:
    try:
        value = float(amount)
        if value < 0:
            print("Kwota nie może być ujemna.")
            return None
        return value
    except ValueError:
        print(f"Niepoprawna kwota: {amount}. Proszę wprowadzić wartość liczbową.")
        return None