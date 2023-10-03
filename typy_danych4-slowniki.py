# słownik  - {klucz:wartosc}
# typ danych para: klucz - wartosc
# odwzorowanie jsona w pythona
# hrejterzy
# {"name":"Radek"}
# klucz znie moze sie powtarzac

dictionary = {}  # pusty słownik
print(dictionary)  # {}

dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
# dict_values(['Radek', 39])
# dict_keys(['imie', 'wiek'])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

dictionary.update({'date': '12-12-12023'})
print(dictionary)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-12023'}

dictionary1 = {'x': 2}
dictionary1.update([('y', 3), ('z', 5)])
print(dictionary1)  # {'x': 2, 'y': 3, 'z': 5}
print(dictionary1['x'])  # 2 - wypisanie elementu ze słownika

# stworenie słownika polsko - ang
# 3 klucze
# stworzyc słownik z elemntami
# wypisac tłumaczenia dla przykładowego klucza
dict2 = {'imie': 'name', 'kot': 'cat', 'pies': 'dog'}
print(dict2['imie'])  # name

# wypisemy słowa jakie umiemy przetłuamczyc
print('Mam w słowniku', dict2.keys())
key = input("Podaj słówko do przetłumaczenia")  # input - odczytaj np.: z klawiatury
print(dict2[key.replace(" ", "").lower()])  # cat

# kalkulator
# pobrac od uzytkownika a i b (input)
# wypisac wynik np dodawania  (print)
# input zawsze zwraca <class 'str'>
a = int(input("Podaj pierwszą liczbę"))
# b = float(input("Podaj druga liczbę"))
b = input("Podaj druga liczbę")
print(type(a))
print(a + int(b))  # 112.0 float
# print(a + b)  # 112.0 float
