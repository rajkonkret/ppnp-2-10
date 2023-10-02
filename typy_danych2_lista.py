# lista - kolekcja przechowująca dowolną ilość danych
# przechowuje różne typy danych w jedej kolekcji
# zachowuje kolejność dodawania elementów

lista = []  # definicja pustej listy
print(lista)  # []
print(type(lista))  # <class 'list'>

print(bool(lista))  # False

lista.append("Radek")
print(lista)  # ['Radek']
lista.append("Maciek")
lista.append("Jaśko")
lista.append("Zenek")
lista.append("Marta")
print(lista)  # ['Radek', 'Maciek', 'Jaśko', 'Zenek', 'Marta'] 0,1,2,3,4
print(lista)  # ['0(-5)', '1(-4)', '2(-3)', '3(-2)', '4(-1)'] 0,1,2,3,4
# indeksowanie od 0
# ostatni element listy ma również indeks -1
print(lista[0])  # nazwa listy, nawias kwadratowy i w nawiasie indeks
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
# Radek
# Maciek
# Jaśko
# Zenek
# Marta
# print(lista[10])  # IndexError: list index out of range
print(len(lista))  # len() - długość listy 5 ale indeksy od 0 do 4
print(lista[-1])  # Marta
# wypisac elemnty listy za pomocą ujemnych indeksów
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])
# Marta
# Zenek
# Jaśko
# Maciek
# Radek

print(lista[0:3])  # ['Radek', 'Maciek', 'Jaśko'] od indeksu 0 do indeksu 2 zbiór z prawej strony otwarty
print(lista[2:])  # od 2 do końca  ['Jaśko', 'Zenek', 'Marta'] - włacznie z 2
print(lista[:3])  # ['Radek', 'Maciek', 'Jaśko'] od 0..2
print(lista[7:9])  # []
print(lista[1:3])  # ['Maciek', 'Jaśko'] 1..2

# nadpisac elemntu w liscie na ideksie (zastąpić innym)
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek', 'Marta']

# rozszerzenie listy, wstawienie elemntu w konkretne miejsce
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Zenek', 'Marta']

ind = lista.index("Marcin")
print(ind)  # 1
# usunięcie elementu po indeksie
element = lista.pop(ind)
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek', 'Marta']
print(element)  # Marcin

# usniecie po elemencie
element = lista.remove("Maciek")
print(lista)
print(element)  # None nie mamy zwrotnej informacjo kogo usunęliśmy
# None (null) nic, nie wiem, nieokreślony
print(bool(None))  # False

# lista.remove("Kasia")  # ValueError: list.remove(x): x not in list
print('Radek' in lista)  # True element istnieje w liscie
lista.append('Radek')
print(lista)  # ['Radek', 'Mikołaj', 'Zenek', 'Marta', 'Radek']
lista.remove('Radek')
print(lista)  # ['Mikołaj', 'Zenek', 'Marta', 'Radek']
# usunie pierwszy napotkany element

a = 1
b = 3
a = b
print(a)
print(b)
a = 7
print(b)  # 3

lista2 = lista  # kopiuje referencje(adres pamięci)
print(lista)
print(lista2)
lista3 = lista.copy()  # kopije jedna liste do drugiej umieszczając w nowym miejsu w pamięci
lista.clear()  # czysci zawartość listy
print(lista)
print(lista2)  # []
print(lista3)  # ['Mikołaj', 'Zenek', 'Marta', 'Radek']
print()
print(id(lista2))  # wypisanie adresu dla listy
print(id(lista))
# 2106304909376
# 2106304909376
print(id(lista3))  # 2187997668032

liczby = [54, 999, 34, 22, 13.34, 687]
# liczby = [54, 999, 34, 22, 13.34, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(liczby)
print(type(liczby))  # <class 'list'>
liczby.sort()
print(liczby)  # [13.34, 22, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola', 'agata', 'lena']
lista_osoby.sort()
print(lista_osoby)  # ['agata', 'lena', 'ola', 'radek']
lista_osoby.sort(reverse=True)  # sortuje i odwraca kolejnosc
print(lista_osoby)  # ['radek', 'ola', 'lena', 'agata']
lista_osoby.reverse()
print(lista_osoby)  # ['agata', 'lena', 'ola', 'radek']

# naindeksie 3 wpiszemy int 6666
liczby[3] = 6666
print(liczby)  # [13.34, 22, 34, 6666, 687, 999]
#                   -6   -5   -4  -3    -2   -1
print(liczby[0:3])  # [13.34, 22, 34]
print(liczby[-2])  # 687
print(liczby[0:-2])  # [13.34, 22, 34, 6666] 0..4 bez 4 czyli 0..3
print(liczby[-3:0])  # [] w zasadzie błedny zapis bo nie umie z -3 dojsc do zera
print(liczby[-3:])  # [6666, 687, 999]

liczby.remove(34)
print(liczby)
print(liczby.pop(3))  # 687

tekst = "Python"  # lista znaków
lista_1 = list(tekst)  # rozpakowanie sekencji
print(lista_1)  # ['P', 'y', 't', 'h', 'o', 'n']

lista2 = [tekst]
print(lista2)  # ['Python']

print(lista_1 + lista2)  # ['P', 'y', 't', 'h', 'o', 'n', 'Python']

krotka = tuple(liczby)  # krotka, tupla
print(krotka)  # (13.34, 22, 6666, 999)
