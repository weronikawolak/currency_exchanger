from exchangers import CurrencyExchanger
from views import CurrencyView
from providers import NBPDataProvider
from utils import validate_input_currency, validate_input_amount #importuje moduły stworzone  w innych plikach

class Main:
    def __init__(self, exchanger, view, provider): #inicjuje zmienne instancji,moge teraz korzystac z nich w kazdej metodzie klasy, obikety klas, exchanger odpowiedzialny za logike przeliczania walut 
        self.exchanger = exchanger
        self.view = view
        self.provider = provider

    def run(self):
        currencies = self.provider.get_data()
        print("Pobrano kursy walut.")

        #Najpierw aplikacja korzysta z dostawcy danych NBPDataProvider,
        #  aby pobrać aktualne kursy walut z API. Wynik jest przechowywany
        #  w zmiennej currencies jako słownik, gdzie kluczem jest kod waluty 
        # (np. "USD", "EUR"), a wartością jest kurs wymiany.


        # sprawdzamy czy waluta jest dostępna w danych pobranych z API.

        if not currencies:
            print("Nie udało się pobrać danych o walutach.")
            return
        self.view.display_currencies(currencies)

        while True:  
            from_currency = input("Podaj walutę źródłową: ").upper()
            if validate_input_currency(from_currency, currencies):
                break

        while True: 
            to_currency = input("Podaj walutę docelową: ").upper()
            if validate_input_currency(to_currency, currencies):
                break

        while True:  
            amount = input("Podaj kwotę: ")
            validated_amount = validate_input_amount(amount)
            if validated_amount is not None:  # Jeżeli wartość jest poprawna (czyli nie jest None)
                amount = validated_amount  # Przypisz poprawną wartość
                break

        print(f"Wprowadzono walutę źródłową: {from_currency}, walutę docelową: {to_currency}, kwotę: {amount}")  

        result = self.exchanger.exchange(amount, from_currency, to_currency, currencies)
        self.view.display_conversion(amount, from_currency, to_currency, result) #chcemy wyświetlić wynik przeliczenia w czytelny sposób
        print(f"Przeliczono kwotę {amount} {from_currency} na {result} {to_currency}")  


# Uruchomienie aplikacji
if __name__ == "__main__":
    exchanger = CurrencyExchanger()
    view = CurrencyView()
    provider = NBPDataProvider()
    app = Main(exchanger, view, provider)
    app.run()