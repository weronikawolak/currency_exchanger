from typing import Dict
from interfaces import ICurrencyView

# Implementacja widoku w konsoli
class CurrencyView(ICurrencyView):
    def display_currencies(self, currencies: Dict[str, float]) -> None:
        print("Dostępne kursy walut:")
        for currency, rate in currencies.items():
            print(f"{currency}: {rate:.4f}")

    def display_conversion(self, amount: float, from_currency: str, to_currency: str, result: float) -> None:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")