# Currency_exchanger
The Currency Exchanger is a Python-based program designed to facilitate real-time currency conversion using the latest exchange rates from external providers. The system allows users to convert an entered amount from one currency to another, using live exchange rates fetched from various sources. The program is structured with modularity in mind, making it easy to extend, modify, and integrate into other financial applications.

The program follows a structured process: first, it prompts the user to enter a source currency, a target currency, and an amount to be converted. Then, it connects to predefined exchange rate providers, retrieves the latest rate, and performs the currency conversion. The calculated result is displayed to the user along with additional information, such as the exact exchange rate used. The system is also equipped with error handling, ensuring that users do not input invalid currency codes and that they are notified in case of network failures or provider unavailability.

# Features and functionalities:

- **Real-time exchange rates** – the system fetches up-to-date exchange rates to provide the most accurate conversions.
- **Multiple data sources** – the application supports multiple exchange rate providers, allowing for greater flexibility and reliability.
- **Automatic error handling** – if the user inputs an invalid currency code or if an API request fails, the system will handle the error and notify the user.
