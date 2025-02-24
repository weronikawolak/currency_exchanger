import requests #biblioteka do żądan HTTP
from typing import Dict
from interfaces import ICurrencyCollectionProvider, IDataProvider

# Singleton dla klasy CurrencyCollectionProvider, tzn prywatna zmienna klasy przechowujaca jedyna instancje klasy
class CurrencyCollectionProvider(ICurrencyCollectionProvider):
    _instance = None

    def __new__(cls):
        if cls._instance is None: #zanim utworztmy to sprawdzamy czy jest
            cls._instance = super(CurrencyCollectionProvider, cls).__new__(cls)
        return cls._instance
    

    def get_currency_data(self) -> Dict[str, float]:
        response = requests.get("https://api.nbp.pl/api/exchangerates/tables/a/")
        response.encoding = 'utf-8'
        if response.status_code != 200:
            print(f"Błąd podczas pobierania danych: {response.status_code}")
            return {}

        data = response.json() #konwersja z json na slownik
        currencies = {} # tworzymy pusty slownik

           # Przetwarzanie danych z API
        for rate in data[0]['rates']:
            currencies[rate['code']] = rate['mid']  # 'code' to kod waluty, 'mid' to kurs średni

        currencies['PLN'] = 1.0  # PLN jako jednostka bazowa
        return currencies

# Implementacja pobierania danych z NBP
class NBPDataProvider(IDataProvider):
    def get_data(self) -> Dict[str, float]:
        provider = CurrencyCollectionProvider()
        return provider.get_currency_data()