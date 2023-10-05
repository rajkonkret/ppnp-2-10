# REST API -  GET, POST,PUT, DELETE [HEAD]
# odpowiednik w bazie danych select, insert, update, delete
# CRUD - create, read, update, delete
import requests as re

# pip install requests

# url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'
url = 'http://api.nbp.pl/api/exchangerates/rates/A/THB/'
# url = 'http://api.nbp.pl/api/exchangerates/tables/B/'
#  {'currency': 'peso kolumbijskie', 'code': 'COP', 'mid': 0.001047}, 2023-10-04
response = re.get(url)
print(response)
# <Response [200]> - ok
# 3XX - błedy konfiguracji np przekierowania
# 4XX - 404 - brak zasobu, 400 Bad Request
# 5Xx - wewnetrzne błedy serwera np.: bład bazy danych

table = response.json()
print(table)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '193/A/NBP/2023', 'effectiveDate': '2023-10-05', 'mid': 4.3768}]}
# wypisac wartości wszystkich kluczy ze słownika
print(table['table'])
print(table['currency'])
print(table['code'])
print(table['rates'])  # [{'no': '193/A/NBP/2023', 'effectiveDate': '2023-10-05', 'mid': 4.3768}]
print(table['rates'][0])  # {'no': '193/A/NBP/2023', 'effectiveDate': '2023-10-05', 'mid': 4.3768}
print(table['rates'][0]['no'])
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])  # 4.3768
# Komunikaty błędów
# W przypadku braku danych dla prawidłowo określonego zakresu czasowego zwracany jest komunikat 404 Not Found
# W przypadku zadania nieprawidłowo sformułowanych zapytań serwis zwraca komunikat 400 Bad Request
# W przypadku zapytania przekraczającego limit zwracanych danych serwis zwróci komunikat
# 400 Bad Request - Przekroczony limit
