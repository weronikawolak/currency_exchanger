from abc import ABC, abstractmethod
from typing import Dict

# Interfejs ICurrencyCollectionProvider
class ICurrencyCollectionProvider(ABC):
    @abstractmethod
    def get_currency_data(self) -> Dict[str, float]:
        pass

# Interfejs ICurrencyView
class ICurrencyView(ABC):
    @abstractmethod
    def display_currencies(self, currencies: Dict[str, float]) -> None:
        pass

    @abstractmethod
    def display_conversion(self, amount: float, from_currency: str, to_currency: str, result: float) -> None:
        pass

# Interfejs IExchanger
class IExchanger(ABC):
    @abstractmethod
    def exchange(self, amount: float, from_currency: str, to_currency: str, currencies: Dict[str, float]) -> float:
        pass

# Interfejs IDataProvider
class IDataProvider(ABC):
    @abstractmethod
    def get_data(self) -> Dict[str, float]:
        pass