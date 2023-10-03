dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}
print(type(dictionary))

# wypisuje klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)
# imie
# nazwisko
# imie
# nazwisko

# wypisanie wartosci
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisanie par
for i in dictionary.items():
    print(i)  # ('nazwisko', 'Kowalski')

# rozpakowana para klucz wartość
for k, v in dictionary.items():
    print(k, '=>', v)
# imie => Radek
# nazwisko => Kowalski

dictionary2 = {'name': 'imie', 'company': 'rozne'}
print({value: key for key, value in dictionary2.items()})
# {'imie': 'name', 'rozne': 'company'}
d2 = {}
for key, value in dictionary2.items():
    d2[value] = key
print(d2)  # {'imie': 'name', 'rozne': 'company'}
print({value: key for key, value in dictionary2.items()})