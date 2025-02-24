from typing import Dict
from interfaces import IExchanger

# Implementacja logiki przeliczania walut
class CurrencyExchanger(IExchanger):
    def exchange(self, amount: float, from_currency: str, to_currency: str, currencies: Dict[str, float]) -> float:
        if from_currency not in currencies or to_currency not in currencies:
            raise ValueError("Niepoprawny kod waluty.")
        from_rate = currencies[from_currency]
        to_rate = currencies[to_currency]
        
        result = (amount * from_rate) / to_rate
        return result
    
    # słownik, w którym klucz to kod waluty, a wartosc to kurs wymiany
    